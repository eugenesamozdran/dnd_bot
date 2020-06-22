import mysql.connector

class Db_connect:

    def __init__(self, user='*****', password='*****', database='*****'):
        self.user = user
        self.password = password
        self.database = database

    def __enter__(self):
        self.con = mysql.connector.connect(
            user=self.user, 
            password=self.password, 
            database=self.database
        )
        self.curs = self.con.cursor()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.curs.close()
        self.con.close()
        

def get_value(condition): 
    # receives a string argument equal to some primary key in db table
    # and returns its description from another column
    
    with Db_connect() as manager:
        stmt = 'SELECT con_description FROM conditions WHERE con_name = "{}"'.format(condition)
        manager.curs.execute(stmt)
        result = manager.curs.fetchall()
        return result[0][0]

def get_pkey(): 
    # forms a list of primary key values from database

    with Db_connect() as manager:
        stmt = 'SELECT con_name FROM conditions'
        manager.curs.execute(stmt)
        result = manager.curs.fetchall()
        pkey_list = [i[0] for i in result]
        return pkey_list
