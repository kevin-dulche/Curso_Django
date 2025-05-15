# Protección de Datos Sensibles con Django Environ

## Resumen

Aprender a manejar información sensible es crucial para la seguridad de cualquier proyecto. Jango facilita este proceso mediante su librería Django Environment, la cual permite gestionar credenciales fuera del archivo de configuración principal.

## ¿Cómo instalar Django Environment?

Para comenzar, instala Django Environment desde la terminal usando el comando:

```Bash
pip install django-environ
```

Luego, ve a tu archivo `settings.py` y añade la importación de la librería al principio del archivo:

```Python
import environ
```

## ¿Cómo configurar las variables de entorno?

Primero, crea una nueva instancia de la librería y define las variables en el archivo `settings.py`:

```Python
env = environ.Env()
```

Luego, mueve tus credenciales sensibles a un archivo `.env` en la raíz del proyecto, asegurándote de no subir este archivo al repositorio:

```
DATABASE_PASSWORD=my_secure_password
```

En `settings.py`, reemplaza las credenciales directas con las variables de entorno:

```Python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT'),
    }
}
```

## ¿Cómo cargar las variables de entorno?

Para que Django reconozca el archivo `.env`, debes cargarlo en tu configuración. Agrega la siguiente línea en la parte superior de `settings.py`:

```Python
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
```

Esto permitirá que las variables definidas en `.env` sean accesibles desde el entorno de Django.

## ¿Qué hacer si la variable no se carga?

Si las variables no se cargan automáticamente, puedes exportarlas manualmente en tu entorno antes de ejecutar el servidor de Django:

```Bash
export DATABASE_PASSWORD=my_secure_password
```

## ¿Cómo simplificar la configuración de la base de datos?

Django Environment ofrece métodos útiles como `db_url` que simplifican aún más la configuración:

```Python
DATABASES = {
    'default': env.db(),
}
```

Define todas las credenciales en una única variable en el archivo .env:

```
DATABASE_URL=postgres://user:password@host:port/dbname
```

Este método reduce el número de configuraciones manuales, facilitando la administración de variables.

## ¿Qué ventajas ofrece Django Environment?
Usar Django Environment para gestionar credenciales ofrece múltiples beneficios:

* **Seguridad mejorada:** Mantén credenciales fuera del código fuente.
* **Facilidad de uso:** Simplifica la configuración de la base de datos.
* **Colaboración segura:** Permite compartir código sin exponer información sensible.