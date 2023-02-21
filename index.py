import sqlite3
from sqlite3 import Error
import pdb

"""
Pour la création de la base de données, le repertoire doit être créé
"""
#print('Bonjour avec SQLite')
dbFile=r"C:\sqlite\db\pythonsqlite.db"
def createConnection(file):
    connection=None
    try:
        connection=sqlite3.connect(file)
        print(sqlite3.version)
        print("Connexion établie avec succès")
        return connection
    except  Error as e:
        print("Erreur "+str(e))
    
    return connection

def deleteInformation(conn,id):
    query="""DELETE FROM persons WHERE id=?"""
    cursor=conn.cursor()
    cursor.execute(query,(id,))
    conn.commit()

def selectInfoFromDataBase(conn):
    query="""SELECT * FROM persons"""
    cursor=conn.cursor()
    cursor.execute(query)
    
    result=cursor.fetchall()
    
    for value in result:
        print(value)

def updateInfoOfDataBase(conn,value):
    query="""UPDATE persons SET name=?, first_name=?,number=?, address=? WHERE id=?"""
    cursor=conn.cursor()
    cursor.execute(query,value)
    conn.commit()
    print("Information mise à jour avec succès")

def insertIntoTable(conn,value):
    query="INSERT INTO persons(name,first_name,number,address) VALUES(?,?,?,?)"
    cursor=conn.cursor()
    
    cursor.execute(query,value)
    conn.commit()
    print("Information ajoutée avec succès")
    return cursor.lastrowid

def createTable(conn,dbFile):
    #print("Table créée")
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS persons (id integer PRIMARY KEY,name text NOT NULL,first_name text NOT NULL,number text NOT NULL,address text NOT NULL);"""
    c=conn.cursor()
    c.execute(sql_create_projects_table)

#Call of functions
conn=createConnection(dbFile)
"""
values=("KOFFI","KOUASSI","023154214","80, RUE DE GALILEE, 75021 NANTESS")
insertIntoTable(conn,values)

values_one=("EVRARD","KOUASSI","021484854","32, RUE DE MERMOZ, 69010 LION")
insertIntoTable(conn,values_one)

values_two=("TRAORE","JEAN","05412510","210, AVENUE DE GALILEE, 10210 MARSEILLE")
insertIntoTable(conn,values_two)

values_three=("KOFFI","KOUASSI","01210214","150, AVENUE DU GLE LECLERC, 88210 LILLES")
insertIntoTable(conn,values_three)
"""
#createTable(conn,dbFile)

#selectInfoFromDataBase(conn)

#valueToUpdate=("JOSE","LANDRY","062541444","117, RUE DE LA FOLIE, 75021 Parish",1)
#updateInfoOfDataBase(conn,valueToUpdate)

#deleteInformation(conn,4)