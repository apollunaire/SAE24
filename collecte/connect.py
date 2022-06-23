import mysql.connector
from mysql.connector import Error
import MySQLdb


def ajoutCapteur(macadd, piece):
    try:
        id = "-1"
        queryText = "SELECT id, macadd from capteur where macadd='" + macadd + "'"
        cursor.execute(queryText)
        myresult = cursor.fetchall()

        if len(myresult) == 0:
            print(f"le capteur {macadd} n'existe pas")
            queryinsert = "INSERT INTO capteur(macadd, piece) VALUES(%s %s)"
            val = (macadd, piece)
            cursor.execute(queryinsert, val)
            connection.commit()
            print("OK")

            queryText = "SELECT id, macadd, from capteur where macadd='" + macadd + "'"
            cursor.execute(queryText)
            myresult = cursor.fetchall()
            id = myresult[0][0]
        else:
            print("Le capteur existe avec l'id", myresult[0])
            id = myresult[0][0]

        return id

    except MySQLdb.Error as e:
        print("Exception : ", e)


def democapteur():
    macadd = "WEB"
    piece = "Maison1"
    date = "12/12/12"
    heure = "12:30"
    valeur = "1.5"
    id = ajoutCapteur(macadd, piece)
    print(f"id={id}")

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='mysqldb',
                                         user='toto',
                                         password='toto', use_pure=True)

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL database... MySQL Server version on ", db_Info)
        cursor = connection.cursor()

        ajoutCapteur(democapteur())


except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        print("test")
        connection.close()
        print("MySQL connection is closed")