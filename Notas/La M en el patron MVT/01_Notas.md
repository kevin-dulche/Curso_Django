# Introducción a Modelos y Bases de Datos

## Resumen

La “M” en el patrón MVC se refiere al Modelo, que es crucial para manejar datos de la base de datos en Django. En lugar de utilizar listas con datos estáticos en las vistas, ahora trabajaremos con datos provenientes del modelo, aprovechando el ORM de Django.

## ¿Qué es el ORM en Django?

El ORM (Object-Relational Mapping) en Django nos permite definir clases de Python que se relacionan directamente con las tablas de la base de datos. De esta forma, evitamos escribir sentencias SQL, ya que todo se maneja mediante Python.

## ¿Cómo se define una clase de modelo en Django?

Para definir un modelo, creamos una clase en el archivo `models.py`. Cada clase de modelo se corresponde con una tabla en la base de datos. Por ejemplo, si definimos la clase `Car`, esta se convertirá en una tabla con el nombre `Car` en la base de datos.

## ¿Qué son las migraciones en Django?

Las migraciones son un sistema que Django usa para aplicar y revertir cambios en la base de datos. Cuando creamos o modificamos un modelo, generamos migraciones que se pueden aplicar para crear o actualizar tablas en la base de datos.

## Aplicar una migración

1. Creamos la clase `Car` con un atributo `title`.
2. Ejecutamos la migración hacia adelante para crear la tabla `Car` en la base de datos.
3. Si agregamos un campo `year` a la clase `Car`, otra migración aplicará este cambio a la tabla.

## Revertir una migración

* Si es necesario, podemos revertir una migración para volver al estado anterior de la tabla.
* Por ejemplo, al revertir la migración del campo `year`, la tabla `Car` quedará como antes de agregar dicho campo.

## ¿Cómo permite Django ser independiente del motor de base de datos?

Django ORM es compatible con varios motores de base de datos. En este curso, utilizaremos SQLite para ejemplos iniciales y PostgreSQL para el proyecto final.