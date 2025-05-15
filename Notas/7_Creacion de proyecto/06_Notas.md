# Django Admin

## Resumen

Explorar la funcionalidad del Django Admin es esencial para aprovechar al máximo el potencial de Django en la gestión de aplicaciones web.

## ¿Qué es el Django Admin?

Django Admin es una herramienta integrada en Django que permite administrar modelos y objetos a través de una interfaz web intuitiva y fácil de configurar.

## ¿Cómo accedemos al Django Admin?

Primero, asegúrate de que el proyecto de Django esté corriendo. Luego, accede a la URL “/admin”. Aparecerá una página de inicio de sesión con el título “Django Administration”.

## ¿Cómo creamos un superusuario?

Para acceder al admin, necesitas un superusuario. Detén el servidor y ejecuta el comando `createsuperuser`. Proporciona un nombre de usuario, correo electrónico y contraseña. Reinicia el servidor y usa estas credenciales para iniciar sesión en el admin.

## ¿Cómo registramos un modelo en el Django Admin?

1. Abre el archivo `admin.py` dentro de tu aplicación.
2. Crea una nueva clase que herede de `admin.ModelAdmin`.
3. Importa tu modelo con from `.models import Product`.
4. Registra el modelo usando `admin.site.register(Product, ProductAdmin)`.

## ¿Cómo personalizamos la vista de lista en el Django Admin?

Puedes añadir campos a la lista de visualización usando `list_display`:

```Python
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
```

Esto muestra los campos `name` y `price` en la lista de productos.

## ¿Cómo agregamos funcionalidad de búsqueda?

Añade el atributo `search_fields` en la clase del administrador:

```Python
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name',)
```

Esto permite buscar productos por nombre.

## ¿Cómo editamos y guardamos productos?

Desde la lista de productos, haz clic en un producto para abrir el formulario de edición. Realiza los cambios necesarios y selecciona una de las opciones de guardado.

## ¿Cómo añadimos imágenes a los productos?

1. Asegúrate de tener un campo de imagen en tu modelo.
2. Sube una imagen a través del formulario de edición.
3. Configura las URLs para servir archivos estáticos agregando la configuración en `urls.py`:

```Python
from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## ¿Cómo administramos múltiples productos?

Selecciona varios productos usando los checkboxes y aplica acciones en masa, como eliminar.

## ¿Cómo configuramos la visualización de imágenes en la lista de productos?

Configura las URLs de los archivos estáticos y media para que Django sepa dónde encontrarlas. Asegúrate de importar y utilizar correctamente `static` y `settings` en tu archivo `urls.py`.

## ¿Cómo agregamos un nuevo campo al modelo?

Para agregar un nuevo campo, como la fecha de creación, modifica el modelo y actualiza la clase del administrador para mostrarlo en la lista:

```Python
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
```