import mysql.connector

def get_value(condition): 
    # receives a string argument equal to some primary key in db table and returns its description from another column
    
    config = {
        'user': 'root', 
        'password': 'Thrashtilldeath92', 
        'database': 'sql_hr'
    }

    con = mysql.connector.connect(**config)
    curs = con.cursor()

    stmt = 'SELECT con_description FROM conditions WHERE con_name = "' + condition + '"'

    curs.execute(stmt)
    result = curs.fetchall()

    return result[0][0]

    curs.close()
    con.close()

def get_pkey(): 
    # forms a list of primary key values from database

    config = {
        'user': 'root', 
        'password': 'Thrashtilldeath92', 
        'database': 'sql_hr'
    }

    con = mysql.connector.connect(**config)
    curs = con.cursor()

    stmt = 'SELECT con_name FROM conditions'

    curs.execute(stmt)
    result = curs.fetchall()

    pkey_list = [i[0] for i in result]
    return pkey_list

    curs.close()
    con.close()
