import csv
import os, glob
import mysql.connector
from mysql.connector import Error
import MySQLdb


def ajoutCapteur(macadd, piece, emplacement, nom):
    connection = mysql.connector.connect(host='localhost',
                                         database='mysqldb',
                                         user='toto',
                                         password='toto', use_pure=True)
    cursor = connection.cursor()
    print("OK connexion")

    try:
        id = "-1"
        queryText = "SELECT id, mac from capteur where mac=" + macadd + ""
        cursor.execute(queryText)
        myresult = cursor.fetchall()
        if len(myresult) == 0:
            print(f"le capteur {macadd} n'existe pas")
            queryinsert = "INSERT INTO capteur(mac, piece, emplacement, nom) VALUES(%s, %s, %s, %s)"
            val = (macadd, piece, emplacement, nom)
            cursor.execute(queryinsert, val)
            connection.commit()
            print("OK")

            queryText = "SELECT id, mac, from capteur where mac=" + macadd + ""
            cursor.execute(queryText)
            myresult = cursor.fetchall()
            id = myresult[0][0]
        else:
            print("Le capteur existe avec l'id", myresult[0])
            id = myresult[0][0]

        return id
    except MySQLdb.Error as e:
        print("Exception : ", e)



def ajoutData(date, temp, macadd):
    connection = mysql.connector.connect(host='localhost',
                                         database='mysqldb',
                                         user='toto',
                                         password='toto', use_pure=True)
    cursor = connection.cursor()
    print("OK connexion")

    try:
        id = "-1"
        queryText = "SELECT macadd, date from temperature where macadd=" + macadd + " and date=" + date + ""
        cursor.execute(queryText)
        myresult = cursor.fetchall()
        if len(myresult) == 0:
            print(f"l'entrée {macadd, date} n'existe pas")
            queryinsert = "INSERT INTO temperature(date, temp, macadd) VALUES(%s, %s, %s)"
            val = (date, temp, macadd)
            cursor.execute(queryinsert, val)
            connection.commit()
            print("OK")

            queryText = "SELECT macadd, date from temperature where macadd=" + macadd + " and date=" + date + ""
            cursor.execute(queryText)
            myresult = cursor.fetchall()
            id = myresult[0][0]
        else:
            print("L'entrée existe avec l'id", myresult[0])
            id = myresult[0][0]

        return id

    except MySQLdb.Error as e:
        print("Exception : ", e)


def democapteur():
    macadd = "A7E33F6B79BB"
    piece = "Maison1"
    emplacement = 'test'
    nom = 'test'
    date = "12/12/12"
    heure = "12:30"
    valeur = "1.5"
    mac = ajoutCapteur(macadd, piece, emplacement, nom)
    print(f"id={id}")

def lecture():
    with open('dataa.csv', encoding='utf-8', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            print(row)
            macadd = row[0]
            piece = row[1]
            emplacement, nom= '', ''
            date = row[2]
            valeur = row[4]
            print(macadd, piece, emplacement, nom)
            #mac = ajoutCapteur(macadd, piece, emplacement, nom)
            t = ajoutData(date, valeur, macadd)
            print(f"id={id}")

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='mysqldb',
                                         user='toto',
                                         password='toto', use_pure=True)

    if connection.is_connected():
        db_Info = connection.get_server_info()
        lecture()
        print("?")
        print("Connected to MySQL database... MySQL Server version on ", db_Info)
        cursor = connection.cursor()


except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")