from mypackages import functions

def selectInfoFromDataBase(conn):
    query="""SELECT * FROM persons"""
    cursor=conn.cursor()
    cursor.execute(query)
    
    result=cursor.fetchall()
    print("---------------------------------------------------------------------------------")
    for value in result:
        print(value)
        print("---------------------------------------------------------------------------------")

dbFile=r"C:\sqlite\db\pythonsqlite.db"
conn=functions.createConnection(dbFile)
selectInfoFromDataBase(conn)