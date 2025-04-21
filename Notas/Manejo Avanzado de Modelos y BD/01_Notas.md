# Gestión de Modelos y Bases de Datos en Django con SQLite

## Resumen

La migración de modelos en Django es un proceso fundamental para mantener la base de datos en sincronía con las clases del proyecto. Este artículo explora el uso de comandos para migrar modelos en Django, específicamente cómo manejar la migración de un modelo llamado “carro”.

## ¿Cómo identificar migraciones pendientes en Django?

Al ejecutar el comando `python manage.py runserver`, puedes encontrar un error que indica migraciones pendientes. Este mensaje significa que las tablas correspondientes a tus clases de Django no están creadas en la base de datos, lo que impide el correcto funcionamiento del proyecto.

## ¿Cómo crear migraciones en Django?

Para crear migraciones, usa el comando `python manage.py makemigrations`. Este comando genera un archivo en la carpeta de migraciones con la creación de la tabla correspondiente al modelo “carro”.

## ¿Cómo aplicar migraciones en Django?

Una vez creadas las migraciones, se deben aplicar usando `python manage.py migrate`. Esto ejecuta todas las migraciones y crea las tablas necesarias en la base de datos.

## ¿Cómo verificar la base de datos en Django?

Puedes revisar la base de datos usando `python manage.py dbshell`. Este comando te conecta a la base de datos definida en el archivo `settings.py`. En este caso, se utilizó SQLite, que es fácil de usar pero no ideal para producción debido a su baja concurrencia.

## ¿Cómo configurar la base de datos en Django?

La configuración de la base de datos se encuentra en el archivo `settings.py` bajo el diccionario `DATABASES`. Django soporta múltiples motores de base de datos como PostgreSQL, MariaDB, MySQL, Oracle y SQLite. En este curso, se utilizará PostgreSQL.