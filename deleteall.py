from mypackages import functions

def deleteAllInformation(conn):
    query="""DELETE FROM persons"""
    cursor=conn.cursor()
    cursor.execute(query)
    conn.commit()
    print("Suppression de tous les élements effectuée avec succès")

dbFile=r"C:\sqlite\db\pythonsqlite.db"
conn=functions.createConnection(dbFile)

deleteAllInformation(conn)