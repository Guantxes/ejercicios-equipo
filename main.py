"""Programa del equipo.

Carga automáticamente todo lo que haya en la carpeta miembros/ y lo muestra.
No hace falta editar este archivo: cada persona solo toca su propio archivo.

Ejecútalo con:  python3 main.py
"""

import importlib
import pkgutil

import config
import miembros


def cargar_miembros():
    """Importa cada archivo de miembros/ (menos los que empiezan por _)."""
    for info in sorted(pkgutil.iter_modules(miembros.__path__), key=lambda i: i.name):
        if info.name.startswith("_"):
            continue
        yield importlib.import_module(f"miembros.{info.name}")


def main():
    print(f"=== Equipo: {config.NOMBRE_EQUIPO} ===")
    modulos = list(cargar_miembros())

    if not modulos:
        print("Todavía no hay nadie en miembros/. ¡Empieza la Ronda 1!")
        return

    for modulo in modulos:
        print(modulo.saludo())
        # La despedida se añade en la Ronda 3 (ramas)
        if hasattr(modulo, "despedida"):
            print("   " + modulo.despedida())


if __name__ == "__main__":
    main()
