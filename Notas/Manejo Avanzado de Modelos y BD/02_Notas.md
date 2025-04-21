# Inserción de Datos con Django

## Resumen

## ¿Cómo se agrega un nuevo campo a una tabla en Django?

Para agregar un nuevo campo a una tabla existente, necesitas modificar la clase del modelo correspondiente. Por ejemplo, si deseas añadir el campo “año” a la clase Carro, lo haces así:

* Añade el campo como un TextField con un MaxLength de 4, ya que solo necesitas almacenar valores como 2022, 2023, etc.

```Python
class Carro(models.Model):
    ...
    año = models.TextField(max_length=4, null=True)
```

## ¿Qué pasos se siguen después de modificar el modelo?

Después de agregar el nuevo campo al modelo, sigue estos pasos:

1. **Guardar los cambios en el archivo del modelo:** No olvides guardar el archivo después de realizar modificaciones.
2. **Crear nuevas migraciones:** Ejecuta el comando `python manage.py makemigrations`. Si no detecta cambios, verifica si guardaste el archivo.
3. **Aplicar las migraciones:** Ejecuta `python manage.py migrate`. Este comando actualiza la base de datos con la nueva estructura.

## ¿Cómo se soluciona el error de campo no nulo?
Si intentas crear un campo no nulo en una tabla que ya contiene datos, Django te pedirá resolver cómo manejar los registros existentes. Puedes:

* Proveer un valor por defecto.
* Permitir valores nulos.

En este ejemplo, se permite que el campo “año” sea nulo (`null=True`), para evitar problemas con registros anteriores.

## ¿Cómo se utiliza el ORM de Django para interactuar con los datos?

Una vez aplicado el nuevo campo, puedes usar el ORM de Django para interactuar con la base de datos. Usamos el comando `python manage.py shell` para acceder al shell interactivo de Django.

Ejemplo de cómo crear un nuevo registro:

1. **Importar el modelo:**

```Python
from my_first_app.models import Car
```

2. **Crear una instancia de Carro:**

```Python
nuevo_carro = Car(titulo='BMW', año='2023')
```

3. **Guardar la instancia en la base de datos:**

```Python
nuevo_carro.save()
```

## ¿Cómo mejorar la visualización de los objetos en el shell?

Define el método `__str__` en tu modelo para que la representación textual del objeto sea más clara:

```Python
class Carro(models.Model):
    ...
    def __str__(self):
        return f"{self.titulo} - {self.año}"
```

## ¿Cómo agregar un nuevo atributo y practicar?

Añadir un nuevo atributo, como el color del carro, sigue los mismos pasos:

1. Modifica la clase del modelo para incluir el nuevo campo.
2. Guarda el archivo.
3. Ejecuta los comandos makemigrations y migrate.
4. Utiliza el shell para crear y guardar nuevos registros con el atributo color.