# Creación del Modelo para la Aplicación 'Products' en Django

## Resumen

Crear una aplicación de administración de productos en una cafetería puede parecer complejo, pero siguiendo unos pasos claros, es más sencillo de lo que parece. En este artículo, exploraremos cómo crear y configurar un modelo de producto utilizando Django.

## ¿Cómo creamos la aplicación de productos?

Para empezar, debemos crear una nueva aplicación dentro de nuestro proyecto de Django. Desde la consola, ejecutamos los siguientes comandos:

* Manage
* Startup
* Products

Esto generará una nueva carpeta llamada “products”. Recuerda siempre registrar las aplicaciones creadas. Vamos a `settings`, buscamos `INSTALLED_APPS` y añadimos `products`.

## ¿Cómo definimos los modelos?

Después de registrar la aplicación, procedemos a crear los modelos. Iniciamos con el modelo `Product` que hereda de `Model`. El primer campo será `Name`, definido como un `TextField` con un `MaxLength` de 200 caracteres.

## ¿Qué es Verbose Name y cómo lo utilizamos?

El `Verbose Name` nos permite especificar cómo queremos que se visualice cada campo para el usuario final. Por ejemplo, para `Name` podemos definir un `verbose_name`.

## ¿Qué otros campos añadimos?

Aparte de `Name`, añadimos otros campos importantes:

* `Description`: `TextField` con `MaxLength` de 300.
* `Price`: `DecimalField` con `max_digits` de 10 y `decimal_places` de 2.
* `Available`: `BooleanField` con `default=True`.
* `Photo`: `ImageField` con `upload_to='logos'`, permitiendo valores nulos (`null=True`) y en blanco (`blank=True`).

## ¿Cómo formateamos el código y solucionamos errores de dependencias?

Para mantener el código limpio, utilizamos la extensión `Black`. Hacemos clic derecho, seleccionamos `Format Document Width` y elegimos `Black Formatter`.

Si el editor no encuentra las dependencias, debemos asegurarnos de que Visual Studio Code esté utilizando el entorno virtual correcto. Seleccionamos el entorno correcto en la parte inferior del editor y recargamos la ventana con `Command P` o `Control P` seguido de `reload window`.

## ¿Cómo añadimos un método str?

Para una representación textual del modelo, añadimos un método `__str__` que retorna el nombre del producto.