lista_libros = {}
contador_id = 1

while True:
    print("\n")
    print("\033[1m\033[34m=\033[0m" * 30) 
    print("\033[1m\033[34m=\033[0m" * 30)  
    opciones = int(input("\033[1m\033[32mMenú de Libros\033[0m"  
                         "\n\033[1m\033[33m1\033[0m Agregar Libro"
                         "\n\033[1m\033[33m2\033[0m Consultar Libros"
                         "\n\033[1m\033[33m3\033[0m Eliminar Libro"
                         "\n\033[1m\033[33m4\033[0m Modificar Libro"
                         "\n\033[1m\033[33m5\033[0m Salir"
                         "\n\033[1m\033[35mOpción = \033[0m"))  

    if opciones == 1:
        titulo = input("\n\033[1m\033[36mIngrese Título: \033[0m")  
        autor = input("\033[1m\033[36mIngrese Autor: \033[0m")  
        año = (input("\033[1m\033[36mIngrese Año: \033[0m"))  
       
        libro = {
            "título": titulo,
            "autor": autor,
            "año": año,
        }
        lista_libros[contador_id] = libro
        print(f"\n\033[1m\033[32mLibro agregado con ID {contador_id}\033[0m")  
        contador_id += 1

    elif opciones == 2:
        if lista_libros:
            print("\n\033[1m\033[36mLista de Libros:\033[0m")  
            claves = list(lista_libros.keys())
            i = 0
            while i < len(claves):
                clave = claves[i]
                libro = lista_libros[clave]
                print(f"\n\033[1m\033[33mID:\033[0m {clave}")  
                print(f"\033[1m\033[34mTítulo:\033[0m {libro['título']}")  
                print(f"\033[1m\033[34mAutor:\033[0m {libro['autor']}") 
                print(f"\033[1m\033[34mAño:\033[0m {libro['año']}")  
                i += 1
        else:
            print("\033[1m\033[31mNo hay libros registrados\033[0m")  

    elif opciones == 3:
        if lista_libros:
            try:
                id_eliminar = int(input("\033[1m\033[36mIngrese el ID del libro a eliminar: \033[0m"))  
                if id_eliminar in lista_libros:
                    del lista_libros[id_eliminar]
                    print("\033[1m\033[32mLibro eliminado correctamente\033[0m") 
                else:
                    print("\033[1m\033[31mID no encontrado\033[0m")  
            except ValueError:
                print("\033[1m\033[31mID inválido\033[0m")  
        else:
            print("\033[1m\033[31mNo hay libros\033[0m")  

    elif opciones == 4:
        if lista_libros:
            try:
                id_modificar = int(input("\033[1m\033[36mIngrese el ID del libro que desea modificar: \033[0m"))  
                if id_modificar in lista_libros:
                    libro = lista_libros[id_modificar]

                    nuevo_titulo = input("\033[1m\033[36mIngrese nuevo título (Enter para mantener): \033[0m")  
                    if nuevo_titulo:
                        libro["título"] = nuevo_titulo

                    nuevo_autor = input("\033[1m\033[36mIngrese nuevo autor (Enter para mantener): \033[0m")  
                    if nuevo_autor:
                        libro["autor"] = nuevo_autor

                    nuevo_año = input("\033[1m\033[36mIngrese nuevo año (Enter para mantener): \033[0m")  
                    if nuevo_año:
                        libro["año"] = nuevo_año

                    print("\033[1m\033[32mLibro modificado correctamente\033[0m")  
                else:
                    print("\033[1m\033[31mID ingresado incorrecto\033[0m")  
            except ValueError:
                print("\033[1m\033[31mID inválido\033[0m") 
        else:
            print("\033[1m\033[31mNo hay libros para modificar\033[0m")  

    elif opciones == 5:
        print("\n\033[1m\033[35mSaliendo del programa\033[0m")  
        break

    else:
        print("\n\033[1m\033[31mOpción inválida\033[0m") 