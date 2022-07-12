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
        "(6) Revisar ventas de procutos semanales") # SE POSPONE TODAVIA NO SE HACE noo
        option = int(input(""))
        while option != 0:
            if option == 1:
                cursor.execute("select name,stock from items where")
                listaDeStock = cursor.fetchall()
                
                for fila in listaDeStock:
                    print(fila[0] + " stock : " + str(fila[1]))
                break    

            elif option == 2:
                print("")
            elif option == 3:
                print(" 1.- Intel Core i5-12400 \n 2.- Intel Core i3 10105 \n 3.- Intel Core i3-10100F \n 4.- RTX 3080 XLR8 \n 5.- PNY GeForce RTX 3070 \n 6.- PNY GeForce RTX 3050 ")
                id = int(input("Que producto desea comprar?: "))
                cursor.execute("select name,stock from items")
                listaDeStock = cursor.fetc()

                for fila in listaDeStock:
                    print(fila[0],fila[1])
                break
                

            elif option == 4:
                print("")
            elif option == 5:
                print("")

        
             
    if __name__ == "__main__":
        main()

