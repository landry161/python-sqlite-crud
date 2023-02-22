#connection
import sqlite3
from sqlite3 import Error

dbFile=r"C:\sqlite\db\pythonsqlite.db"
def createConnection(file):
    connection=None
    try:
        connection=sqlite3.connect(file)
        #print(sqlite3.version)
        #print("Connexion établie avec succès")
        return connection
    except  Error as e:
        print("Erreur de connexion")
        print("Erreur "+str(e))
    
    return connection