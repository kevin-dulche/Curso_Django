# Desarrollo de Vistas Genéricas en Django

## Resumen

## ¿Cómo crear una interfaz para los usuarios finales?

En una aplicación para cafeterías es esencial tener interfaces separadas para los empleados y los clientes finales. Este diseño asegura que la información sensible se mantenga privada. Comencemos creando una interfaz adecuada para los usuarios finales, donde puedan ver su pedido sin acceder a otros datos.

## ¿Qué pasos seguir para integrar el botón "Mi Pedido"?

El botón "Mi Pedido" es crucial para que los clientes puedan revisar sus pedidos. Aquí tienes una guía detallada sobre cómo implementarlo en tu aplicación Django:

1. **Revisar el botón en el template:** Asegúrate de que el botón "Mi Pedido" tenga asignada una URL específica. En este caso, no tenía ninguna URL, por lo que se usó un numeral.

2. **Configurar las URLs de la aplicación:** Dirígete al archivo urls.py de tu aplicación Orders. Crea una nueva ruta:

```Python
path('myorder/', views.MyOrderView.as_view(), name='my_order')
```

3. **Crear la vista específica:** Dentro del archivo `views.py`, crea una nueva vista que heredará de `DetailView` para obtener y mostrar un objeto específico.

```Python
from django.views.generic import DetailView
from .models import Order

class MyOrderView(DetailView):
    model = Order
    template_name = 'orders/my_order.html'
    context_object_name = 'order'
```

## ¿Cómo personalizar la vista para mostrar solo una orden activa?

Personalizar la vista permite mejorar la experiencia del usuario gracias a una presentación precisa y ajustada:

* Modificar el método `get_object` para que filtre por la orden activa, sin requerir directamente el ID en la URL.

```Python
def get_object(self, queryset=None):
    return Order.objects.filter(is_active=True).first()
```

## ¿Qué recursos adicionales son útiles para configurar vistas genéricas en Django?

Para profundizar en el uso de vistas genéricas en Django, te recomendamos explorar el sitio web ccbb.co.uk, donde encontrarás documentación y ejemplos detallados sobre cómo utilizarlas eficientemente.

## ¿Cómo mejorar la experiencia del usuario en la plantilla HTML?

Para que los pedidos se muestren adecuadamente se requiere una estructura HTML limpia y efectiva:

## ¿Cómo extender las plantillas base en Django?

Crea un archivo `my_order.html` dentro de una nueva carpeta `templates/orders`:

```HTML
{% extends 'base.html' %}

{% block content %}
  {% if order %}
    <h2>Detalles de tu pedido</h2>
    <p>Usuario: {{ order.user.username }}</p>
    <p>Fecha: {{ order.order_date|date:"SHORT_DATE_FORMAT" }}</p>
    <ul>
      {% for line_item in order.orderproduct_set.all %}
        <li>{{ line_item.product.name }} - ${{ line_item.product.price }}</li>
      {% empty %}
        <p>No hay elementos en tu pedido.</p>
      {% endfor %}
    </ul>
  {% else %}
    <p>No hay pedidos activos.</p>
  {% endif %}
{% endblock %}
```

## ¿Cómo configurar el debug para solucionar problemas?

Para identificar errores en el template, usa el tag `{% debug %}` sobre el contexto para ver todas las variables disponibles. Recuerda eliminar el debug una vez solucionado el problema.

## ¿Cómo asegurar que solo el usuario autorizado vea su orden?

Aunque hemos implementado el detalle de la orden, es vital garantizar que cada usuario solo vea sus propios pedidos. Aquí te dejo un desafío:

* **Ajustar el filtro de la query:** Asegúrate de que la orden mostrada corresponde al usuario autenticado.

Para ello, en el método `get_object`, filtra por el usuario actual usando `request.user`. ¡Manos a la obra, mejora tu código y continua aprendiendo sobre Django para crear aplicaciones más robustas!