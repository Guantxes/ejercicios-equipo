# Ejercicios en equipo: Git

Vais a trabajar en grupos de 3-4 personas sobre un mismo proyecto de Python: una **batalla de luchadores**.
Cada uno crea el suyo, y entre todos lo juntáis con Git. No hace falta saber programar: solo cambiar unos valores.
Cada ronda enseña algo real del trabajo en equipo con Git.

**Qué necesitas:** Git con tu clave SSH ya configurada (`ssh -T git@github.com` te saluda por tu usuario), Python 3 y VS Code.
En Windows, todo desde la terminal de **WSL** y dentro de `~/` (nunca en `/mnt/c`).

> Pregunta a quien presenta si algo no sale. Si algo da error, **leed el mensaje**: casi siempre dice qué hacer.

---

## Ronda 0: Preparar el equipo (15 min)

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

5. Cuando hayáis aceptado la invitación, clonad **el repo del responsable** (no el de la organización). Cambia `USUARIO_DEL_RESPONSABLE` por el usuario de GitHub **del responsable** (pídeselo: no es el tuyo):
   ```
   git clone git@github.com:USUARIO_DEL_RESPONSABLE/ejercicios-equipo.git
   cd ejercicios-equipo
   ```

**Todos:** abrid el proyecto en VS Code con `code .` y comprobad que funciona:

```
python3 main.py
```

Debe decir "Todavía no hay nadie en miembros/".

---

## Ronda 1: Todos suben a la vez (10 min)

Vais a añadir cada uno **vuestro propio luchador**, en su archivo. Como nadie toca el archivo de otro, no hay conflicto, pero Git os va a parar igualmente: es lo normal cuando varios suben a la vez.

1. Copia la plantilla con tu nombre (minúsculas, sin tildes):
   ```
   cp miembros/_plantilla.py miembros/tunombre.py
   ```
2. Abre tu archivo en VS Code y cambia los tres valores: `NOMBRE` (el de tu luchador, puede ser un apodo), `VIDA` (máx. 30) y `ATAQUE` (máx. 8).
3. Comprueba que funciona: `python3 main.py` (hace falta que haya al menos dos luchadores para pelear; mientras tanto te dirá que esperes rivales)
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

5. Descarga lo de tus compañeros, júntalo con lo tuyo y vuelve a subir:
   ```
   git fetch
   git merge origin/main
   git push
   ```
   `git fetch` solo descarga lo nuevo y no toca tus archivos; `git merge origin/main` lo junta con lo tuyo.
   Si se abre un editor pidiendo un mensaje de merge, guarda y cierra (en nano: `Ctrl+O`, `Enter`, `Ctrl+X`).
6. Ejecuta `python3 main.py`. ¡Deberían pelear todos los luchadores del equipo!

**Para pensar:** ¿por qué el `git merge` no dio conflicto? (Pista: mirad `git log --oneline --graph`.)

---

## Ronda 2: Ramas y Pull Request (15 min)

Hasta ahora todos habéis trabajado directamente sobre `main`. En equipos reales eso es peligroso: un fallo tuyo rompe el trabajo de todos. La solución son las **ramas**.

1. Asegúrate de estar al día:
   ```
   git fetch
   git merge origin/main
   ```
2. Crea **tu propia rama**:
   ```
   git checkout -b tunombre-grito
   ```
3. En tu archivo `miembros/tunombre.py`, añade una línea al final con el grito de guerra de tu luchador:
   ```python
   GRITO = "¡Nadie me gana a piedra, papel o tijera!"
   ```
4. Guarda y sube **tu rama** (no `main`):
   ```
   git add miembros/tunombre.py
   git commit -m "Añado grito de guerra de tunombre"
   git push -u origin tunombre-grito
   ```
5. En la web de GitHub, entra en el repo: verás un botón verde **Compare & pull request**. Ábrelo, ponle título y descripción, y créalo.
6. **Revisión cruzada:** un compañero abre tu Pull Request, mira *Files changed* y, si está bien, pulsa **Merge pull request**.
7. Vuelve a `main` y trae los cambios:
   ```
   git checkout main
   git fetch
   git merge origin/main
   python3 main.py
   ```
   Cuando todos hayáis hecho merge de vuestros PR, `main.py` mostrará el grito de guerra de cada luchador antes del combate.

¡Y ya está! Podéis seguir jugando: subid la vida, probad otro ataque, inventad un luchador nuevo... siempre en una rama y con Pull Request.

---

## Ronda 3: el torneo (al final de la charla)

Cuando os lo indiquen, vuestro luchador se apunta al torneo de **todos los equipos**: https://github.com/skillIssu3/torneo-luchadores

Las instrucciones (fork, rama y Pull Request) están en el README de ese repositorio. Antes de empezar, ten al día este repo, porque de aquí copiarás tu luchador a `luchadores/tuusuario.py`:

```
git checkout main
git fetch
git merge origin/main
```

Los dos repositorios tienen que estar en la misma carpeta (por ejemplo `~/git`).

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
- `CONFLICT ... Automatic merge failed`: Git no sabe cuál de dos cambios en la misma línea elegir. Abre el archivo en VS Code, deja solo la versión buena (botones *Accept...*), y luego `git add`, `git commit`, `git push`. Si te agobias: `git merge --abort`.
- `Need to specify how to reconcile divergent branches`: has usado `git pull`. En esta práctica usamos `git fetch` y luego `git merge origin/main`.
- `cannot run less: No such file or directory` o `unable to execute pager 'less'`: tu sistema no tiene el programa `less`, que Git usa para paginar. Ejecuta una vez `git config --global core.pager cat` y repite el comando.
- `remote: Permission to ... denied`: estás intentando subir al repo de la organización en vez del de tu responsable. Revisa `git remote -v`.
