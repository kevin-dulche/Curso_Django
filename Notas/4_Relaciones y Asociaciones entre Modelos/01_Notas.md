# Creación y Gestión de Relaciones entre Modelos en Django

## Resumen

Aprender a relacionar tablas es fundamental para manejar datos interconectados en Django

## ¿Cómo crear la clase Publisher?

Para iniciar, creamos la clase `Publisher` que hereda de `models.Model`. Incluimos atributos como `name` y `address` utilizando `models.TextField` con un `max_length` de 200, un valor que puedes ajustar según tus necesidades de datos.

```Python
class Publisher(models.Model):
    name = models.TextField(max_length=200)
    address = models.TextField(max_length=200)

    def __str__(self):
        return self.name
```

## ¿Cómo definir la clase Book?

La clase `Book` también hereda de `models.Model` y contiene atributos como `title`, `publication_date` y `publisher`. Utilizamos `models.DateField` para manejar fechas y establecemos una relación con `Publisher` usando `models.ForeignKey`.

```Python
class Book(models.Model):
    title = models.TextField(max_length=200)
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
```

## ¿Cómo relacionar Book con Publisher usando ForeignKey?

La relación se establece con `models.ForeignKey`, donde especificamos el modelo relacionado (`Publisher`) y el comportamiento al eliminar (`on_delete=models.CASCADE`). Esto asegura que si un editor se elimina, también se eliminarán sus libros.

## ¿Cómo aplicar migraciones?

Para aplicar estos cambios a la base de datos, creamos y aplicamos las migraciones con los comandos:

```Bash
python manage.py makemigrations
python manage.py migrate
```

## ¿Cómo usar la shell interactiva?

Para facilitar la interacción con la base de datos, instalamos `ipython` con:

```Bash
pip install ipython
```

Esto mejora la experiencia en la shell permitiendo autocompletar y otras funcionalidades útiles.

## ¿Cómo crear y guardar registros en la shell?

Dentro de la shell, primero creamos un `Publisher` y luego un `Book` relacionado.

```Python
from myapp.models import Publisher, Book

publisher = Publisher(name="Editorial Example", address="123 Main St")
publisher.save()

book = Book(title="Two Scoops of Django", publication_date="2024-07-17", publisher=publisher)
book.save()
```