from unicodedata import name
from conexionDB import conexionDB


class index:
    def main(): 
        conexion = conexionDB()
        con = conexion.conn
        cursor = con.cursor()
        

        print("Hola, Bienvenido a la interfaz, Porfavor seleccione una opción")
        print("(1) Consultar Stock\n" +
        "(2) Mostrar lista de productos para ver su caracteristicas\n"+ # Blank
        "(3) Acceder a la interfaz Agregar de venta de productos \n"+ #pablo SOLO HACER UNA VENTA QUE SE REFLEJE EN EL STOCK DEL PRODUCTO 
        "(4) Historial de ventas de productos\n" + #SE POSPONEN TODAVIA NOS SE HACE
        "(5) Interfaz Agregar, eliminar y editar productos\n"+ # BLANK AGREGAR // PABLO ELIMINAR // FUKA EDITAR
        "(6) Revisar ventas de procutos semanales") # SE POSPONE TODAVIA NO SE HACE
        option = int(input(""))
        while option != 0:
            if option == 1:
                cursor.execute("select name,stock from items where") #borren el where de la query !!!!!!!!!!!!!!!
                listaDeStock = cursor.fetchall()
                
                for fila in listaDeStock:
                    print(fila[0] + " stock : " + str(fila[1]))
                break    

            elif option == 2:
                print("")
            elif option == 3:
                print("")
            elif option == 4:
                print("")
            elif option == 5:
                print("____________________________________")
                print("(1) Agregar producto")
                print("(2) Editar Producto")
                print("(3) Eliminar Producto")
                print("(4) <- Volver")
                seleccion = int(input())
                if seleccion == 1:
                    print("blank culiao XD")
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
                    

    if __name__ == "__main__":
        main()

