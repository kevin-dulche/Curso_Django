# Personalización de Interfaz con Plantillas en Django

## Resumen

Exploraremos los templates en Django y sus funcionalidades avanzadas que los diferencian del HTML estándar. Aprenderemos cómo los templates nos permiten mostrar contenido dinámico en el navegador, validar variables, recorrer listas y aplicar filtros para modificar valores antes de mostrarlos. También veremos cómo reutilizar contenido común mediante el archivo base HTML.

## ¿Qué son los templates en Django?

Los templates en Django son archivos HTML que incluyen funcionalidades adicionales para mostrar contenido dinámico. A diferencia del HTML puro, los Django templates permiten:

* Mostrar variables
* Realizar validaciones con `if`
* Recorrer listas con `for`

## ¿Cómo se muestran variables en un template?

Para mostrar variables, se encierran en dobles llaves `{{ }}`. Por ejemplo, para mostrar una variable llamada `var` del contexto, se usaría:

```HTML
{{ var }}
```

## ¿Qué son y cómo se utilizan los filtros en Django?

Los filtros permiten modificar el valor de una variable antes de mostrarla. Se usan con un pipe `|` seguido del nombre del filtro. Por ejemplo, para mostrar solo el día y mes de una fecha:

```HTML
{{ fecha_nacimiento|date:"m/d" }}
```

Los filtros pueden concatenarse. Por ejemplo, convertir el resultado en minúsculas:

```HTML
{{ fecha_nacimiento|date:"m/d"|lower }}
```

## ¿Qué son los tags en Django y cómo se utilizan?

Los tags agregan funcionalidades adicionales al código HTML. Se abren con `{% %}` y pueden incluir:

* `if`: para validaciones
* `for`: para recorrer listas
* `url`: para mostrar URLs dinámicas

Algunos tags requieren una etiqueta de cierre. Por ejemplo, `if` y `for`:

```HTML
{% if condition %}
    <!-- contenido -->
{% endif %}
```

## ¿Qué es el archivo base HTML en Django?

El archivo `base.html` permite definir contenido común para ser reutilizado en la aplicación. Se crean bloques que pueden extenderse en otros archivos. Por ejemplo:

```HTML
<!-- base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    <div id="content">
        {% block content %}
        {% endblock %}
    </div>
</body>
</html>
```

Para reutilizar este contenido:

```HTML
<!-- new_template.html -->
{% extends "base.html" %}
{% block content %}
    <!-- contenido específico -->
{% endblock %}
```