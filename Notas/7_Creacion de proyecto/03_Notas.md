# Cómo Crear Migraciones de Datos en Django

## Resumen

Nuestro modelo de producto ha sido actualizado con un nuevo campo: image field. Al intentar crear las migraciones, el sistema muestra un error indicando que no se puede usar image field porque Pillow no está instalado. No hay que preocuparse, la solución es instalar Pillow. Siguiendo la sugerencia del error, ejecutamos `pip install Pillow`. Ahora, volvemos a correr `makemigrations` y el error desaparece, logrando así la primera migración de nuestra aplicación de productos.

## ¿Cómo se soluciona el error al crear migraciones?

El error ocurre porque Pillow, una librería necesaria para manejar campos de imagen, no está instalada. La solución es instalarla con `pip install Pillow`.

## ¿Qué hacemos después de instalar Pillow?

Después de instalar Pillow, es importante:

* Verificar que funciona corriendo nuevamente make migrations.
* Asegurarse de agregar la dependencia a `requirements.txt` para evitar problemas en producción. Utiliza pip freeze para ver la versión instalada y añade Pillow al archivo.

## ¿Por qué es importante agregar Pillow a requirements.txt?

Cuando instalamos dependencias localmente, debemos asegurarnos de que estén en requirements.txt para que también se instalen en el entorno de producción. Esto se hace para evitar errores y asegurar que todas las librerías necesarias estén disponibles.

## ¿Qué permite hacer Pillow con los campos de imagen?

Pillow permite realizar validaciones en imágenes, como asegurarse de que las imágenes subidas cumplan con ciertas características en cuanto a resolución.

## ¿Qué sigue después de las migraciones?

Después de realizar las migraciones, tienes la base para construir vistas, conectarlas a URLs y crear un listado de productos. Te animo a que lo intentes, lo subas a tu repositorio y compartas el enlace en el sistema de comentarios.