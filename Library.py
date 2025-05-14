

catalogo = [ ] # 

def add_book():
    titulo = input("Ingresa el titulo del libro: ").strip()
    autor = input("Ingresa el nombre del autor del libro: ").strip()

    try:
        cantidad = int(input("Ingresa la cantidad de libros : "))
        precio = float(input("Ingresa el precio del libro: "))

        if cantidad <= 0 or precio <=0:
            print("El precio y la cantidad debe ser superior a 0")
            return
    except ValueError:
        print("Debes ingresar un número") 
        return
    
    catalogo.append({"titulo":titulo,"autor":autor,"cantidad":cantidad,"precio":precio})
    
    print("Libro agregado exitosamente.\n")


    def find_book():
        consulta = input("Ingresa el nombre del libro o el autor a consultar: ").strip().lower()
        encontrado = False
        for libro in catalogo:
            if consulta in libro["titulo"].lower() or consulta in libro["autor"].lower():
                show_book(libro)
                encontrado = True
            if not encontrado:
                print("Libro no encontrado. ")

    def show_book(libro):
        print("Detalles del libro")
        print(f"Título: {libro['titulo']}")
        print(f"Titulo: {libro['autor']}")
        print(f"Titulo: {libro['cantidad']}")
        print(f"Titulo: {libro['precio']}")

    def menu_main():
        while True:
            print("1. Añadir libro")
            print("2. Buscar libro")
            opcion = input("Ingresa una opción: ").strip()
    
            if opcion == '1':
                add_book()
            elif opcion == '2':
                find_book()



    if __name__ =="__main__":
        menu_main()    