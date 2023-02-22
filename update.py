from mypackages import functions

def updateInfoOfDataBase(conn,value):
    query="""UPDATE persons SET name=?, first_name=?,number=?, address=? WHERE id=?"""
    cursor=conn.cursor()
    cursor.execute(query,value)
    conn.commit()
    print("Mise à jour avec succès")

dbFile=r"C:\sqlite\db\pythonsqlite.db"
conn=functions.createConnection(dbFile)

valueToUpdate=("JOSE","LANDRY","062541444","117, RUE DE LA FOLIE, 75021 Parish",1)
updateInfoOfDataBase(conn,valueToUpdate)