from conexionDB import conexionDB


class index:
    def main(): 
        conexion = conexionDB()
        records=conexion.records
        print("Hola, Bienvenido a la interfaz, Porfavor seleccione una opción")
        print("(1) Consultar Stock\n" +
        "(2) Mostrar lista de productos para ver su caracteristicas\n"+
        "(3) Acceder a la inter Agregarfaz de venta de productos \n"+
        "(4) Historial de ventas de productos\n" +
        "(5) Interfaz Agregar, eliminar y editar productos\n"+
        "(6) Revisar ventas de procutos semanales")
        option = int(input(""))
        while option != 0:
            if option == 1:
                for row in records:
                    print(row[3])
            elif option == 2:
                print("")
            elif option == 3:
                print("")
            elif option == 4:
                print("")
            elif option == 5:
                print("")
             
    if __name__ == "__main__":
        main()
