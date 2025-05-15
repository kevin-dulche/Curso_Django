# Configuración del Proyecto en Django

## Resumen

Comenzamos la configuración de un proyecto Coffee Shop en Django

## ¿Cómo crear y activar el entorno virtual?

Para iniciar, nos posicionamos en la carpeta deseada en nuestro editor. Creamos el entorno virtual con:

```Bash
python -m venv <ruta_donde_guardar>/Coffee_Shop
```

Activamos el entorno con:

```Bash
source Coffee_Shop/bin/activate
```

Verificamos su activación y procedemos a instalar Django:

```Bash
pip install django
```

¿Cómo iniciar un proyecto Django?

## Creamos el proyecto utilizando el comando:

```Bash
django-admin startproject coffee_shop .
```

Listamos las carpetas para confirmar la creación del proyecto. Abrimos el proyecto en Visual Studio Code:

```Bash
code -r coffee_shop
```

Ahora tenemos el archivo `manage.py` y las configuraciones listas en nuestro editor.

## ¿Qué extensiones instalar en Visual Studio Code?

Aprovechamos las alertas de Visual Studio Code para instalar extensiones esenciales como:

1. **Python**
2. **PyLance**
3. **Python Debugger**
4. **Black** (formateo de código)
5. **Django** (para visualizar templates)

## ¿Cómo configurar el control de versiones con Git?

Inicializamos un repositorio Git:

```Bash
git init
```

Añadimos y comiteamos los archivos iniciales creados por Django:

```Bash
git add .
git commit -m "Initial setup"
```

## ¿Cómo crear y utilizar un archivo .gitignore?

Para evitar subir archivos innecesarios al repositorio, generamos un archivo `.gitignore` con **gitignore.io** especificando “Django” como criterio. Pegamos el contenido generado en un nuevo archivo `.gitignore` y lo comiteamos:

```Bash
git add .gitignore
git commit -m "Add .gitignore"
```

## ¿Cómo manejar las dependencias del proyecto?

Creamos dos archivos para gestionar las dependencias:

1. **requirements.txt**: para dependencias de producción.
2. **requirements-dev.txt**: para dependencias de desarrollo como `iPython`.

Agregamos las dependencias instaladas en nuestro entorno actual:

```Bash
pip freeze > requirements.txt
```

Comiteamos ambos archivos:

```Bash
git add requirements.txt requirements-dev.txt
git commit -m "Add requirements files"
```

## ¿Cómo continuar con la configuración del proyecto?

Con el entorno preparado, es importante crear un archivo base HTML que sirva como plantilla. Te reto a crear `base.html` con un menú y un pie de página para usar en el curso de Django.