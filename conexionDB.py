class conexionDB:
    import mysql.connector #En CMD poner "pip install mysql-connector-python"

    #Tienen que tener la base de datos "pythontienda" que el fuka tienes que pasarles e implementarla en su phpmyadmin

    conn = mysql.connector.connect(host="localhost",port="3306",user="root",password="", database="pythontienda")
