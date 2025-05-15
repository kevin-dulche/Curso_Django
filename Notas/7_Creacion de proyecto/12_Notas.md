# Creación de APIs con Django REST Framework

## Resumen

La separación de la lógica de backend y frontend es una práctica común en el desarrollo de software moderno, con el frontend generalmente escrito en JavaScript y la conexión al backend manejada a través de APIs. Django REST es una librería de Python que facilita la creación de estas APIs, permitiendo una integración eficiente entre frontend y backend.

## ¿Cómo instalar Django REST Framework?

Para instalar Django REST Framework, utilizamos el siguiente comando:

```Bash
pip install django-rest-framework
```

No olvides agregarlo a tu archivo `requirements.txt` para mantener un registro de las dependencias del proyecto. Además, debes incluirlo en la configuración del proyecto dentro del archivo `settings.py` en la sección de `INSTALLED_APPS`:

```Python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

## ¿Cómo configurar un Serializer en Django REST?

Los Serializers en Django REST convierten modelos de Django en JSON. Para crear un nuevo Serializer, sigue estos pasos:

1. Crea un archivo llamado `serializers.py` en la aplicación correspondiente.
2. Importa `ModelSerializer` desde `rest_framework`:

```Python
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
```

## ¿Cómo crear una vista en Django REST?

Para crear una vista que devuelva datos en formato JSON:

1. Crea una vista heredando de `APIView`:

```Python
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

class ProductListAPI(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
```

2. Define la URL para esta vista en `urls.py`:

```Python
from django.urls import path
from .views import ProductListAPI

urlpatterns = [
    ...
    path('api/products/', ProductListAPI.as_view(), name='product-list-api'),
]
```

## ¿Cómo manejar permisos y autenticación en Django REST?

Dependiendo de tu caso de uso, puedes configurar permisos y autenticación. Para esta vista, vamos a desactivarlos:

```Python
from rest_framework.permissions import AllowAny

class ProductListAPI(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
```

## ¿Cómo ejecutar y probar tu API?

Una vez configurado todo, puedes ejecutar tu servidor de desarrollo y acceder a la URL de la API para ver los datos en formato JSON:

```Bash
python manage.py runserver
```

Luego, visita `http://localhost:8000/productos/api/` para ver la lista de productos.