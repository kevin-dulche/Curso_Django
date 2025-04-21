# Qué es el patrón MVT (Model, View y Template)

## Resumen

### ¿Cómo se definen los modelos en Django?

Los modelos en Django se utilizan para guardar datos. Crearemos una clase llamada `Carro`, que hereda de `models.Model`. Esta clase tendrá un campo `title` de tipo `models.TextField`, con un `max_length` definido para limitar la cantidad de texto que puede aceptar.

```Python
from django.db import models

class Carro(models.Model):
    title = models.TextField(max_length=255)
```

### ¿Cómo se definen las vistas en Django?

Las vistas en Django se encargan de buscar datos y devolverlos al template. Una vista se define como un método que recibe un `request` y retorna una `response`. Usaremos `render` para pasar el request y el template a la vista.

```Python
from django.shortcuts import render

def myView(request):
    car_list = [{'title': 'BMW'}, {'title': 'Mazda'}]
    context = {'car_list': car_list}
    return render(request, 'myFirstApp/carlist.html', context
```

### ¿Cómo se crean y utilizan los templates en Django?

Los templates son archivos HTML que reciben datos de las vistas. Para que Django los reconozca, creamos una carpeta llamada `templates` dentro de nuestra aplicación y luego otra con el nombre de la aplicación. Dentro, creamos el archivo `carlist.html`.

```HTML
<html>
<head>
    <title>Car Listtitle>
</head>
<body>
    <h1>Lista de Carrosh1>
    <ul>
    {% for car in car_list %}
        <li>{{ car.title }}</li>
    {% endfor %}
    </ul>
</body>
</html>
```
### ¿Cómo se registran las aplicaciones en Django?

Para que Django reconozca nuestra nueva aplicación, debemos agregarla a la lista `INSTALLED_APPS` en el archivo `settings.py`.

```Python
INSTALLED_APPS = [
    ...
    'myFirstApp',
]
```

### ¿Cómo se configuran las URLs en Django?

Creamos un archivo `urls.py` en nuestra aplicación y definimos la ruta para nuestra vista. Luego, incluimos esta configuración en el archivo `urls.py` principal del proyecto.

```Python
from django.urls import path
from .views import myView

urlpatterns = [
    path('carlist/', myView, name='carlist'),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myFirstApp/', include('myFirstApp.urls')),
]
```

### ¿Cómo se conectan las vistas y templates en Django?

Pasamos los datos desde la vista al template usando un contexto. En el template, usamos etiquetas Django para iterar sobre los datos y mostrarlos.

```Python
{% for car in car_list %}

{{ car.title }}

{% endfor %}
```