# Curso Django

Django es un framework para desarrollo web escrito en Python que inicialmente fue utilizado para crear blogs, pero ha evolucionado para soportar aplicaciones complejas, como las primeras versiones de Instagram y Spotify. Su popularidad se debe a su facilidad de uso y la rapidez con la que permite desarrollar aplicaciones funcionales.

## ¿Cuáles son los requerimientos previos para aprender Django?

* Conocer Python, ya que Django está construido en este lenguaje.
  - Sintaxis básica: if, for, definición de variables.
* Comprender la programación orientada a objetos.
  - Reutilización de código mediante clases y herencia.
* Conocer HTML para diseñar la interfaz de usuario.
* Conocimientos básicos de CSS para estilizar la aplicación.

## ¿Por qué es importante usar entornos virtuales en Django?
Los entornos virtuales permiten gestionar diferentes versiones de paquetes y librerías en un mismo equipo sin conflictos. Esto es crucial cuando se trabaja en múltiples proyectos que requieren distintas versiones de Django o cualquier otro paquete de Python.

## ¿Cómo se crea un entorno virtual en Python?
Abre la terminal en tu editor de código preferido, como Visual Studio Code.
Crea una carpeta para tu proyecto y ábrela en el editor.
Usa la librería `venv` de Python para crear un entorno virtual:

```bash
python -m venv my_first_env
```
Verifica la creación del entorno con ls en la carpeta especificada.
¿Cómo se activa un entorno virtual?
Para activar el entorno virtual y asegurarte de que los comandos se ejecuten en este entorno específico:

```bash
source ./my_first_env/Scripts/activate # En windows
source ./my_first_env/bin/activate # En Linux
```

Notarás que el nombre del entorno virtual aparece en la terminal, indicando que está activo.

## ¿Qué significa tener un entorno virtual activo?
Significa que cualquier comando que ejecutes utilizará las librerías instaladas en ese entorno específico, evitando conflictos con otras versiones de librerías que puedas tener en tu sistema. Esta práctica es esencial para evitar colisiones y mantener un entorno de desarrollo limpio y manejable.