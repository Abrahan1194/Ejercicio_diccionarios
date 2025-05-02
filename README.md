# Ejercicio_diccionarios
# Gestión de Libros en Python

Este script en Python permite gestionar una lista de libros, ofreciendo las siguientes funcionalidades a través de un menú interactivo:

* **Agregar Libro:** Permite ingresar el título, autor y año de publicación de un nuevo libro, el cual se añade a la lista con un ID único.
* **Consultar Libros:** Muestra la lista de todos los libros registrados, incluyendo su ID, título, autor y año de publicación.
* **Eliminar Libro:** Permite eliminar un libro de la lista especificando su ID.
* **Modificar Libro:** Permite editar la información (título, autor o año) de un libro existente, identificándolo por su ID.
* **Salir:** Finaliza la ejecución del programa.

## Cómo usar el script

1.  **Guarda el código:** Guarda el código Python en un archivo con extensión `.py` (por ejemplo, `gestor_libros.py`).
2.  **Ejecuta el script:Abre una terminal o línea de comandos, navega hasta el directorio donde guardaste el archivo y ejecuta el siguiente comando:
    ```bash
    python gestor_libros.py
    ```
3.  **Interactúa con el menú:** El programa mostrará un menú con las opciones disponibles. Ingresa el número de la opción que deseas realizar y sigue las instrucciones que se te indiquen.

## Notas

* Los libros se almacenan en un diccionario en memoria (`lista_libros`). Los datos se perderán al cerrar el programa.
* Cada libro recibe un ID único y secuencial al ser agregado.
* El script incluye manejo básico de errores para la entrada de IDs al eliminar o modificar libros.
* Se utilizan códigos de escape ANSI para dar color al texto en la terminal, lo cual puede no ser compatible con todas las terminales.
