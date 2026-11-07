# Ejercicios en equipo: Git

Vais a trabajar en grupos de 3-4 personas sobre un mismo proyecto de Python.
Cada ronda enseña un problema real de trabajar en equipo y cómo Git lo resuelve.

**Qué necesitas:** Git con tu clave SSH ya configurada (`ssh -T git@github.com` te saluda por tu usuario), Python 3 y VS Code.
En Windows, todo desde la terminal de **WSL** y dentro de `~/` (nunca en `/mnt/c`).

> Pregunta a quien presenta si algo no sale. Si algo da error, **leed el mensaje**: casi siempre dice qué hacer.

---

## Ronda 0: Preparar el equipo (5 min)

Un solo miembro del grupo hace de **responsable**. El resto espera al paso 5.

**Responsable:**

1. Clona este repositorio:
   ```
   git clone git@github.com:skillIssu3/ejercicios-equipo.git
   cd ejercicios-equipo
   ```
2. En la web de GitHub, crea un repositorio **vacío** y **sin README** en tu cuenta, llamado `ejercicios-equipo`.
3. Apunta tu copia a tu nuevo repo y súbela:
   ```
   git remote set-url origin git@github.com:TU_USUARIO/ejercicios-equipo.git
   git remote -v
   git push -u origin main
   ```
4. En tu repo de GitHub: **Settings > Collaborators > Add people**, e invita a tu equipo. Cada uno debe **aceptar la invitación** (llega por correo y en la campana de GitHub).

**Resto del equipo:**

5. Cuando hayáis aceptado la invitación, clonad **el repo del responsable** (no el de la organización):
   ```
   git clone git@github.com:USUARIO_DEL_RESPONSABLE/ejercicios-equipo.git
   cd ejercicios-equipo
   ```

**Todos**, una sola vez en vuestra máquina:

```
git config --global pull.rebase false
```

(Le dice a Git cómo juntar cambios cuando hacéis `git pull`. Sin esto, Git se queja en la Ronda 1.)

Abrid el proyecto en VS Code con `code .` y comprobad que funciona:

```
python3 main.py
```

Debe decir "Todavía no hay nadie en miembros/".

---

## Ronda 1: Todos suben a la vez (10 min)

Vais a añadir cada uno **vuestro propio archivo**. Como nadie toca el archivo de otro, no hay conflicto, pero Git os va a parar igualmente.

1. Copia la plantilla con tu nombre (minúsculas, sin tildes):
   ```
   cp miembros/_plantilla.py miembros/tunombre.py
   ```
2. Abre tu archivo en VS Code y cambia `TU_NOMBRE` por tu nombre.
3. Comprueba que funciona: `python3 main.py`
4. Guárdalo en Git y súbelo:
   ```
   git status
   git add miembros/tunombre.py
   git commit -m "Añado a tunombre"
   git push
   ```

**Todos a la vez, a la de tres.** Los primeros en subir lo conseguirán. El resto verá:

```
! [rejected]  main -> main (fetch first)
```

No es un error grave: el repositorio remoto tiene commits que tú no tienes. Hay que traerlos primero.

5. Descarga lo de tus compañeros y vuelve a subir:
   ```
   git pull
   git push
   ```
   Si se abre un editor pidiendo un mensaje de merge, guarda y cierra (en nano: `Ctrl+O`, `Enter`, `Ctrl+X`).
6. Ejecuta `python3 main.py`. Debería saludar todo el equipo.

**Para pensar:** ¿por qué `git pull` no dio conflicto? (Pista: mirad `git log --oneline --graph`.)

---

## Ronda 2: Conflicto (10 min)

Ahora todos vais a editar **la misma línea** de **el mismo archivo**: `config.py`.

1. Asegúrate de estar al día: `git pull`
2. Abre `config.py` y cambia el nombre del equipo por el que tú prefieras:
   ```python
   NOMBRE_EQUIPO = "Los Pingüinos"
   ```
3. Súbelo:
   ```
   git add config.py
   git commit -m "Propongo nombre de equipo"
   git push
   ```
4. Quien suba el primero lo consigue. **Los demás** harán `git pull` y verán:
   ```
   CONFLICT (content): Merge conflict in config.py
   Automatic merge failed; fix conflicts and then commit the result.
   ```
5. Prueba a ejecutar `python3 main.py`. Python también se queja por las marcas `<<<<<<<` que Git ha metido en el archivo.
6. Abre `config.py` en VS Code. Verás botones sobre el conflicto: **Accept Current Change**, **Accept Incoming Change** y **Accept Both Changes**.
   - *Current* = tu versión. *Incoming* = la de tus compañeros.
   - **Hablad entre vosotros** y decidid un único nombre. Dejad solo una línea, sin marcas `<<<<<<<`, `=======` ni `>>>>>>>`.
7. Termina el merge:
   ```
   git add config.py
   git commit -m "Resuelvo el conflicto del nombre"
   git push
   ```
   (Si el `push` vuelve a fallar porque otro llegó antes: otro `git pull` y `git push`.)
8. Todos: `git pull` y `python3 main.py`. Tiene que salir el mismo nombre para todo el equipo.

---

## Ronda 3: Ramas y Pull Request (15 min)

Hasta ahora todos habéis trabajado directamente sobre `main`. En equipos reales eso es peligroso: un fallo tuyo rompe el trabajo de todos. La solución son las **ramas**.

1. Asegúrate de estar al día: `git pull`
2. Crea **tu propia rama**:
   ```
   git checkout -b tunombre-despedida
   ```
3. En tu archivo `miembros/tunombre.py`, añade una función nueva:
   ```python
   def despedida():
       return "Hasta luego, soy TU_NOMBRE."
   ```
4. Guarda y sube **tu rama** (no `main`):
   ```
   git add miembros/tunombre.py
   git commit -m "Añado despedida de tunombre"
   git push -u origin tunombre-despedida
   ```
5. En la web de GitHub, entra en el repo: verás un botón verde **Compare & pull request**. Ábrelo, ponle título y descripción, y créalo.
6. **Revisión cruzada:** un compañero abre tu Pull Request, mira *Files changed* y, si está bien, pulsa **Merge pull request**.
7. Vuelve a `main` y trae los cambios:
   ```
   git checkout main
   git pull
   python3 main.py
   ```
   Cuando todos hayáis hecho merge de vuestros PR, `main.py` mostrará la despedida de todo el equipo.

---

## Si algo sale mal

| Comando | Para qué sirve |
|---|---|
| `git status` | Qué está pasando ahora mismo. **Es lo primero que hay que mirar.** |
| `git log --oneline --graph` | Historial de commits en forma de árbol |
| `git remote -v` | A qué repositorio estás conectado |
| `git branch` | En qué rama estás (la marcada con `*`) |
| `git diff` | Qué has cambiado y todavía no has preparado con `add` |
| `git merge --abort` | Cancela un merge con conflictos y vuelve a como estabas |

**Errores habituales**

- `Permission denied (publickey)`: tu clave SSH no está bien subida a GitHub, o estás clonando con `https://` en vez de `git@github.com:`.
- `Repository not found` al clonar el repo de tu responsable: todavía no has aceptado su invitación.
- `Need to specify how to reconcile divergent branches`: te falta `git config --global pull.rebase false`.
- `remote: Permission to ... denied`: estás intentando subir al repo de la organización en vez del de tu responsable. Revisa `git remote -v`.
