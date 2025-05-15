# Pruebas Unitarias con Django: Validación de Listas y Redirecciones

## Resumen

## ¿Cómo manejar pruebas unitarias en Django?

Cuando trabajamos en equipos grandes de desarrollo, es fundamental garantizar que nuestro código funcione correctamente y no genere problemas al modificar o agregar nuevas funcionalidades. Django, un popular framework web en Python, nos proporciona un conjunto de herramientas para realizar pruebas (testing), una práctica indispensable para asegurar el buen funcionamiento de nuestra aplicación con cada cambio que implementamos. Veamos cómo podemos llevar a cabo pruebas unitarias en una aplicación Django.

## ¿Cómo crear pruebas unitarias para productos en Django?

Una característica esencial de nuestra aplicación, Coffee Shop, es la lista de productos que los usuarios pueden visualizar. Para verificar que esta funcionalidad funcione correctamente, incluso después de realizar cambios en el código, podemos implementar pruebas unitarias siguiendo estos pasos:

1. **Crear un archivo de pruebas:** Usaremos un archivo llamado `Test` en nuestros archivos `tests.py` para definir las pruebas.

2. **Definir clases de prueba:** Creamos una clase en Python que contendrá nuestras pruebas. Esta clase heredará de TestCase.

```Python
from django.test import TestCase
from django.urls import reverse

class ProductListTest(TestCase):
    def test_should_return_200(self):
        url = reverse('list_product')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
```

* En este ejemplo, verificamos que la página de lista de productos regrese un código de estado 200, indicando que cargó correctamente.

3. **Usar breakpoints para debugging:** Los breakpoints son herramientas útiles para detener la ejecución del código y permitir inspeccionar el estado de variables.

```Python
# Insertar un breakpoint
import pdb; pdb.set_trace()

# Podemos usar `response.context` para validar el contexto de respuesta
```

4. **Hacer pruebas para la lista de productos:** Además de verificar el código de estado, podemos evaluar si el contexto contiene productos:

```Python
def test_with_products(self):
    # Crear un producto
    Product.objects.create(name="Test Product", price=10.0, available=True)
    
    url = reverse('list_product')
    response = self.client.get(url)
    
    self.assertEqual(response.context['products'].count(), 1)
```

## ¿Cómo probar funcionalidades de usuario como MyOrder en Django?

Otra funcionalidad clave es la de mostrar órdenes de usuario. Podemos probar dos escenarios: cuando el usuario no está logeado y cuando lo está.

### Usuario no logeado

Queremos redirigir al usuario no autenticado a una página de inicio de sesión.

```Python
class MyOrderViewTest(TestCase):
    def test_no_logged_user_should_redirect(self):
        url = reverse('my_order')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # 302 es el código para redirect
```

### Usuario logeado

Necesitamos verificar que un usuario autenticado pueda acceder a la página de órdenes correctamente.

```Python
from django.contrib.auth import get_user_model

class MyOrderViewTest(TestCase):
    def test_logged_user_access_my_order(self):
        User = get_user_model()
        user = User.objects.create(username="testuser")
        self.client.force_login(user)
        
        url = reverse('my_order')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
```

## Herramientas y recomendaciones al realizar pruebas

* **Usa PDB (Python Debugger):** Al agregar breakpoints, obtienes una interfaz interactiva para revisar el contexto de ejecución.
* **Replica pruebas para diferentes escenarios:** Es vital asegurar que todas las rutas de funcionalidad posibles estén cubiertas.

Django facilita el proceso de testing permitiendo crear pruebas y verificar que las funcionalidades no sufran interrupciones ante cambios. Prueba estas estrategias en tus propios proyectos y agrega más casos de prueba para robustecer tu aplicación. Continuar mejorando esta habilidad es crucial para cualquier profesional de desarrollo web.