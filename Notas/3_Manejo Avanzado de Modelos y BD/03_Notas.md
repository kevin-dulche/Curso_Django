# Actualización y Eliminación de Datos en Django

## Resumen

## ¿Cómo modificar datos de un objeto?

Modificar los datos de un objeto en Django es una parte esencial de la administración de bases de datos. Para cambiar un atributo, primero se accede a él y se le asigna un nuevo valor. Por ejemplo, si se quiere cambiar el `Title` de un objeto `Car` que inicialmente es "BMW" a "Mazda", se usará el siguiente código:

```Python
my_car.title = "Mazda"
```

Es importante tener en cuenta que, aunque el cambio se ha realizado en la memoria, este no se reflejará en la base de datos hasta que se guarde. Este paso es crucial para garantizar que los datos sean persistentes. Para guardar los cambios en la base de datos, se utiliza el método `save()`:

```Python
my_car.save()
```

Este comando ejecuta el guardado sin emitir un mensaje, lo que indica que se ejecutó correctamente.

## ¿Cómo verificar cambios en la base de datos?

Para confirmar que los cambios se han realizado correctamente en la base de datos, se recomienda utilizar comandos SQL dentro de la línea de comandos de Django. Por ejemplo:

```Bash
python manage.py dbshell
```

Dentro de la consola, se puede realizar un `SELECT` para comprobar los datos actualizados:

```SQL
SELECT * FROM my_first_app_car;
```

Asegúrate de incluir el punto y coma al final para ejecutar correctamente el comando SQL. Esto mostrará los registros actuales, verificando así que el título ahora es "Mazda".

## ¿Cómo eliminar objetos de la base de datos?

Django simplifica el proceso de eliminación de objetos dentro de la base de datos. Para eliminar un objeto, puedes seguir estos pasos:

Crear un objeto nuevo (opcional): Antes de eliminar, es útil entender la creación de otro objeto, por ejemplo, un Car con el título "Jeep":

```Python
other_car = Car(title="Jeep")
other_car.save()
```

Tras su creación, puedes ver este nuevo objeto también reflejado con un comando `SELECT`.

1. **Eliminar un objeto existente:** Para eliminar un objeto, se usa el método `delete()`, que retornará una tupla indicando cuántos objetos se eliminaron y de qué tipo:

```Python
my_car.delete()
```

Esta acción eliminará el objeto `my_car` y su cambio será visible mediante un nuevo `SELECT` en la base de datos. Al verificar, solo debe aparecer el "Jeep", habiendo desaparecido el "Mazda" de los registros.

Estos procesos son fundamentales para el manejo de datos en Django y permiten modificar y administrar información de manera eficiente. Recuerda siempre verificar mediante comandos SQL cualquier alteración directa en la base de datos para asegurar que los cambios se reflejan como se espera.