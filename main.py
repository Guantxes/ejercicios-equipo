"""Batalla de luchadores.

Cada persona del equipo añade un luchador en la carpeta miembros/.
Este archivo no hace falta tocarlo: carga a todos los luchadores y los
pone a pelear hasta que solo queda uno en pie.

Ejecútalo con:  python3 main.py
"""
import importlib
import pkgutil
import random

import config
import miembros


def cargar_luchadores():
    """Busca todos los archivos de miembros/ (menos los que empiezan por _)."""
    luchadores = []
    for info in sorted(pkgutil.iter_modules(miembros.__path__), key=lambda i: i.name):
        if info.name.startswith("_"):
            continue
        try:
            modulo = importlib.import_module(f"miembros.{info.name}")
            luchador = {
                "nombre": str(modulo.NOMBRE),
                "vida": min(int(modulo.VIDA), config.MAX_VIDA),
                "ataque": min(int(modulo.ATAQUE), config.MAX_ATAQUE),
                "grito": getattr(modulo, "GRITO", None),  # Ronda 2
            }
        except Exception as error:
            # Un archivo roto no debe tumbar a todo el equipo: se ignora y se avisa.
            print(f"⚠ miembros/{info.name}.py tiene un error y se ignora: "
                  f"{type(error).__name__}: {error}")
            print("  Ábrelo, revísalo (¿falta NOMBRE, VIDA o ATAQUE? ¿comillas sin cerrar?) y vuelve a probar.")
            continue
        if luchador["vida"] < 1 or luchador["ataque"] < 1:
            print(f"⚠ miembros/{info.name}.py: VIDA y ATAQUE deben ser al menos 1. Se ignora.")
            continue
        luchadores.append(luchador)
    return luchadores


def combate(luchadores):
    print("\n--- ¡Empieza el combate! ---")
    ronda = 1
    while len([l for l in luchadores if l["vida"] > 0]) > 1:
        print(f"\nRonda {ronda}")
        for atacante in luchadores:
            vivos = [l for l in luchadores if l["vida"] > 0 and l is not atacante]
            if atacante["vida"] <= 0 or not vivos:
                continue
            objetivo = random.choice(vivos)
            daño = random.randint(1, atacante["ataque"])
            objetivo["vida"] -= daño
            print(f"  {atacante['nombre']} golpea a {objetivo['nombre']} (-{daño})")
            if objetivo["vida"] <= 0:
                print(f"  💀 {objetivo['nombre']} cae derrotado")
        ronda += 1
    return [l for l in luchadores if l["vida"] > 0][0]


def main():
    print("=== Batalla de luchadores ===")
    luchadores = cargar_luchadores()

    if not luchadores:
        print("Todavía no hay nadie en miembros/. ¡Empieza la Ronda 1!")
        return
    if len(luchadores) == 1:
        print(f"Solo está {luchadores[0]['nombre']}. Esperando rivales...")
        return

    print("\nLuchadores:")
    for l in luchadores:
        print(f"  {l['nombre']}  (vida {l['vida']}, ataque {l['ataque']})")
        if l["grito"]:
            print(f"     \"{l['grito']}\"")

    campeon = combate(luchadores)
    print(f"\n🏆 ¡{campeon['nombre']} gana el combate!")


if __name__ == "__main__":
    main()
