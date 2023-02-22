from mypackages import functions

def createTable(conn,dbFile):
    #print("Table créée")
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS persons (id integer PRIMARY KEY,name text NOT NULL,first_name text NOT NULL,number text NOT NULL,address text NOT NULL);"""
    c=conn.cursor()
    c.execute(sql_create_projects_table)
    print("Table créée avec succès")

#Call
dbFile=r"C:\sqlite\db\pythonsqlite.db"
connection=functions.createConnection(dbFile)
createTable(connection,dbFile)