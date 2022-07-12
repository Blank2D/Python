from time import sleep
from unicodedata import name
from conexionDB import conexionDB


class index:
    def main(): 
        conexion = conexionDB()
        con = conexion.conn
        cursor = con.cursor()
        
        seleccion = 1005
        option = 10
        while option != 0:

            print("Hola, Bienvenido a la interfaz, Porfavor seleccione una opción")
            print("(1) Consultar Stock\n" +
            "(2) Mostrar lista de productos para ver su caracteristicas\n"+ # Blank
            "(3) Acceder a la interfaz Agregar de venta de productos \n"+ #pablo SOLO HACER UNA VENTA QUE SE REFLEJE EN EL STOCK DEL PRODUCTO 
            "(4) Historial de ventas de productos\n" + #SE POSPONEN TODAVIA NOS SE HACE
            "(5) Interfaz Agregar, eliminar y editar productos\n"+ # BLANK AGREGAR // PABLO ELIMINAR // FUKA EDITAR
            "(6) Revisar ventas de procutos semanales") # SE POSPONE TODAVIA NO SE HACE noo

            option = int(input(""))
            if option == 1:
                cursor.execute("select name,stock from items ") 
                listaDeStock = cursor.fetchall()
                
                for fila in listaDeStock:
                    print(fila[0] + " stock : " + str(fila[1]))
                sleep (1)
                  


            elif option == 2:
                cursor.execute("Select * from items")
                listaDeStock = cursor.fetchall()
                print("------------------------------------------------------------------------------") 
                for fila in listaDeStock:
                    print("id: " + str(fila[0]) + "\nNombre: " + fila[1] + "\nDescrpción: " +
                     fila[2] + "\nStock: " + str(fila[3]) + "\nprecio: " + str(fila[4]))
                    print("------------------------------------------------------------------------------") 
                sleep(1)

            elif option == 3: #POR TERMINAR
                cursor.execute("select name from items ") 
                listaDeStock = cursor.fetchall()
                contador = 0
                for fila in listaDeStock:
                    contador = contador+1
                    print(str(contador)+".-"+ fila[0])
                id = int(input("Que producto desea comprar?: "))
                cursor.execute("SELECT stock from items where id = " + str(id)) 
                stockNuevo = cursor.fetchall()
                cursor.execute("UPDATE items SET stock = " + str(int(stockNuevo[0][0]-1))+ " where id = " + str(id))
                con.commit()
                cursor.execute("select name,stock from items where id =" + str(id))
                listaDeStock = cursor.fetchall()
                print(listaDeStock)
                sleep(1)
                

            elif option == 4:
                print("")
            elif option == 5:
                while seleccion != 0:
                    print("____________________________________")
                    print("(1) Agregar producto")
                    print("(2) Editar Producto")
                    print("(3) Eliminar Producto")
                    print("(4) <- Volver")
                    seleccion = int(input())
                    if seleccion == 1:
                        print("---------------------------------------------------------")
                        print("Porfavor ingrese el NOMBRE del producto que desea agregar")
                        print("---------------------------------------------------------")

                        nombre1 = str(input())

                        print("--------------------------------------------------------------")
                        print("Porfavor ingrese el DESCRIPCION del producto que desea agregar")
                        print("--------------------------------------------------------------")

                        descripcion = str(input())

                        print("--------------------------------------------------------")
                        print("Porfavor ingrese el STOCK del producto que desea agregar")
                        print("--------------------------------------------------------")
                        
                        stock = input()

                        print("---------------------------------------------------------")
                        print("Porfavor ingrese el PRECIO del producto que desea agregar")
                        print("---------------------------------------------------------")

                        precio = input()

                        cursor.execute("INSERT INTO items(name, description, stock, price) VAlUES('" + nombre1 + "', '" + descripcion + "' , '" + stock + 
                        "' , '" + precio + "' )")

                        con.commit()

                        
                    elif seleccion == 2:
                        cursor.execute("select * from items")
                        listaDeStock = cursor.fetchall()
                        print("¿Qué producto desea editar?")
                        for fila in listaDeStock:
                            print("ID: " + str(fila[0]) + " NOMBRE: " + fila[1])
                        editar = int(input(">>>"))
                        print("¿Qué cosa desea editar?")
                        cursor.execute("show columns from items")
                        listaDeColumnas = cursor.fetchall()
                        contador = 0
                        for columna in listaDeColumnas:
                            contador = contador + 1
                            print("(" + str(contador) + ") " + columna[0].upper())
                        editar2 = int(input(">>>"))
                        if editar2 == 1:
                            print("No se puede editar la ID de un producto")
                        elif editar2 == 2:
                            nombre = input("Ingrese el nuevo nombre del articulo\n>>>")
                            cursor.execute("UPDATE items SET name = '" + nombre + "' where id = " + str(editar))
                            con.commit()
                        elif editar2 == 3:
                            description = input("Ingrese la descripción del articulo\n>>>")
                            cursor.execute("UPDATE items SET description = '" + description + "' where id = " + str(editar))
                            con.commit()
                        elif editar2 == 4:
                            stock = int(input("Ingrese el stock del articulo\n>>>"))
                            cursor.execute("UPDATE items SET stock = " + str(stock) + " where id = " + str(editar))
                            con.commit()
                        elif editar2 == 5:
                            price = int(input("Ingrese el precio del articulo\n>>>"))
                            cursor.execute("UPDATE items SET price = " + str(price) + " where id = " + str(editar))
                            con.commit()

                    elif seleccion == 3:
                        cursor.execute("select name from items ") 
                        listaDeStock = cursor.fetchall()
                        contador = 0
                        for fila in listaDeStock:
                            contador = contador + 1
                            print(str(contador)+fila[0])
                            

                            
                        id = input(int("Ingrese el producto que desea eliminar: "))
                        cursor.execute("DELETE from items where id = " + str(id))
                        con.commit()
                        print("Se borro tu wea")

                        
                    elif seleccion == 4:
                        break 


                    

    if __name__ == "__main__":
        main()
