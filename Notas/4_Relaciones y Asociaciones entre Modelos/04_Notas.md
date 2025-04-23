# Queries y Filtros en Django: Optimización y Estrategias Avanzadas

## Resumen

Los managers en Django son una herramienta poderosa que permite realizar diversas acciones dentro de las listas de objetos de un modelo, como contar, traer el primero o el último elemento, crear nuevos registros y mucho más.

Para contar los autores que están creados, utilizamos el manager por defecto llamado `objects` y el método `count`.

```Python
author_count = Author.objects.count()
print(f"Hay {author_count} autores.")
```

## ¿Cómo traer el primer y último autor creado?

Para obtener el primer y último autor, podemos usar los métodos `first` y `last` del manager `objects`.

```Python
primer_autor = Author.objects.first()
print(f"El primer autor es: {primer_autor.name}")

ultimo_autor = Author.objects.last()
print(f"El último autor es: {ultimo_autor.name}")
```

## ¿Cómo crear nuevos autores con el manager?

Podemos crear un nuevo autor directamente en la base de datos utilizando el método `create` del manager.

```Python
nuevo_autor = Author.objects.create(name="Luis Martínez", birthday="1980-01-01")
print(f"Nuevo autor creado: {nuevo_autor.name}")
```

## ¿Cómo traer una lista de autores?

Para obtener una lista de todos los autores, utilizamos el método `all` del manager, que nos devuelve un queryset.

```Python
autores = Author.objects.all()
for autor in autores:
    print(autor.name)
```

## ¿Cómo filtrar autores?

Podemos filtrar autores utilizando el método `filter`, que permite especificar condiciones basadas en los campos del modelo.

```Python
autores_filtrados = Author.objects.filter(name="Pydanny")
for autor in autores_filtrados:
    print(f"Autor filtrado: {autor.name}")
```

## ¿Cómo borrar un autor filtrado?

Primero, filtramos el autor que queremos borrar y luego aplicamos el método `delete`.

```Python
Author.objects.filter(name="Luis Martínez").delete()
print("Autor borrado.")
```

## ¿Cómo ordenar autores?

Podemos ordenar los autores utilizando el método `order_by`.

```Python
autores_ordenados = Author.objects.order_by('name')
for autor in autores_ordenados:
    print(autor.name)
```