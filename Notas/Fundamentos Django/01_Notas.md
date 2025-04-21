# Qué es Django?

## Resumen

Para instalar Django, primero asegúrate de tener un entorno virtual configurado. Luego, usa el comando `pip install django` para instalarlo. Si no especificas la versión, pip instalará la última disponible compatible con tu versión de Python.

Al ejecutar este comando, verás que Django se instala junto con sus dependencias, necesarias para su funcionamiento. Esto es porque Django reutiliza librerías existentes para ciertas funcionalidades.

## ¿Qué es el comando django-admin y cómo se usa?

Una vez instalado Django, obtienes acceso al comando `django-admin`, que es una herramienta de línea de comandos para administrar tareas relacionadas con Django. Para ver todos los subcomandos disponibles, puedes ejecutar django-admin help.

## ¿Cómo crear un proyecto con django-admin?

El subcomando que más nos interesa es startproject, que se usa para crear un nuevo proyecto Django. Para hacerlo, ejecuta:

`django-admin startproject nombre_del_proyecto .`

Asegúrate de no usar guiones en el nombre del proyecto, ya que Django interpretará eso como un intento de resta en Python. Usa guiones bajos en su lugar.

## ¿Qué archivos se crean con startproject?

El comando `startproject` crea una nueva carpeta con el nombre del proyecto. Dentro de esta carpeta, encontrarás:

* Una subcarpeta con configuraciones del proyecto.
* Un archivo `manage.py`, que sirve para ejecutar comandos específicos del proyecto.

## ¿Cómo usar manage.py?

El archivo `manage.py` se utiliza para comandos que afectan solo al proyecto actual. Para ver los comandos disponibles, ejecuta:

```bash
python manage.py help
```

## ¿Cómo ejecutar el servidor de desarrollo?

Para ver tu aplicación en funcionamiento, usa el comando `runserver`:

```bash
python manage.py runserver
```

Este comando inicia un servidor de desarrollo y te indica la URL y el puerto donde tu aplicación está corriendo. Puedes abrir esta URL en tu navegador para verificar que todo está configurado correctamente.