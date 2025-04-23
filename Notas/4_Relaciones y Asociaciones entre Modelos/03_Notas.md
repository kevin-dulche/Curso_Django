# Relaciones Uno a Uno (1:1) en Django

## Resumen

Explorar la relación uno a uno en Django puede parecer complejo, pero es fundamental para construir aplicaciones sólidas.

## ¿Cómo se crea una clase en Django?

Para empezar, imaginemos que tenemos una clase `Profile` que contiene información pública del autor. Este perfil incluirá:

* Un campo de URL para el sitio web del autor.
* Una biografía con un máximo de 500 caracteres.

Aquí está el código inicial para la clase `Profile`:

```Python
class Profile(models.Model):
    website = models.URLField(max_length=200)
    biography = models.TextField(max_length=500)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
```

## ¿Cómo se maneja la relación uno a uno?

Para relacionar el perfil con el autor, utilizamos `OneToOneField`. Esto asegura que cada autor tenga un solo perfil y viceversa. Además, agregamos el parámetro `on_delete=models.CASCADE` para que si se elimina un autor, también se elimine su perfil.

## ¿Cómo se crean y se sincronizan las migraciones?

1. **Crear migraciones:** Ejecutamos `python manage.py makemigrations`.
2. **Sincronizar con la base de datos:** Usamos `python manage.py migrate`.

## ¿Cómo verificamos la creación de un perfil en la consola de Django?

1. **Abrir la shell de Django:** Ejecutamos `python manage.py shell`.
2. **Importar los modelos:** `from myapp.models import Author, Profile`.
3. **Buscar un autor existente:** `author = Author.objects.first()`.
4. Crear un perfil:

```Python
profile = Profile.objects.create(
    website="http://example.com",
    biography="Lorem Ipsum",
    author=author
)
```

## ¿Cómo verificar los datos en la base de datos?

Usamos comandos SQL para verificar los datos:

```SQL
SELECT * FROM myapp_profile WHERE author_id = 1;
```

## ¿Qué ocurre cuando se elimina un autor?

Si un autor se borra, su perfil también se eliminará gracias a `on_delete=models.CASCADE`.