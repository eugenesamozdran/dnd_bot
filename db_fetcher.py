import mysql.connector

def get_value(condition): # receives a string argument and returns corresponding value from db
    
    config = {
        'user': '****', 
        'password': '****', 
        'database': '****'
    }

    con = mysql.connector.connect(**config)

    # print('connected to database')

    curs = con.cursor()

    stmt = 'SELECT con_description FROM conditions WHERE con_name = "' + condition + '"'

    curs.execute(stmt)
    result = curs.fetchall()

    return result[0][0]

    curs.close()
    con.close()
