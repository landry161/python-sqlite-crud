from mypackages import functions

def deleteInformationById(conn,id):
    query="""DELETE FROM persons WHERE id=?"""
    cursor=conn.cursor()
    cursor.execute(query,(id,))
    conn.commit()
    print("Suppression effectuée avec succès")

dbFile=r"C:\sqlite\db\pythonsqlite.db"
conn=functions.createConnection(dbFile)

deleteInformationById(conn,2)