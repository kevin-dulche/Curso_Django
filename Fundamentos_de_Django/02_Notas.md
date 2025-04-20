# Arquitectura de Django

## Resumen

La arquitectura del framework está diseñada para ser reutilizable y organizar todas tus tareas. Utiliza el modelo MVT (Model, View, Template).

## ¿Qué es el modelo en MVT (Model, View, Template)?

El modelo es la parte de los datos:

* Guarda y procesa los datos.
* Contiene la lógica del negocio, como una calculadora que suma 2 más 2.

## ¿Qué es la vista en MTV?

La vista actúa como un conector:

* Accede y dirige los datos.
* Controla el flujo de peticiones y respuestas.
* Verifica permisos y realiza comprobaciones necesarias.

## ¿Qué es el template en MTV?

El template maneja la parte gráfica:

* Usa HTML y CSS para mostrar los datos.
* Por ejemplo, muestra una lista de zapatos almacenada en el modelo.

## ¿Cómo interactúan modelo, vista y template?

El flujo de datos es el siguiente:

* El modelo pasa datos a la vista en un array.
* La vista pasa esos datos al template en un contexto.
* El template muestra los datos gráficos.

En sentido contrario:

* Un usuario busca en el template.
* La vista recibe la búsqueda y consulta al modelo.
* El modelo devuelve los resultados a la vista.
* La vista envía los datos al template para mostrarlos.

**Nota:** No debe haber conexión directa entre template y model. Siempre usa la vista para asegurar verificaciones y permisos.