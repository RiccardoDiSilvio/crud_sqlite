import sqlite3
connection = sqlite3.connect("db.sqlite3")
cursor = connection.cursor()

def create(table, values):
    try:
        cursor.execute("INSERT into {} VALUES {}".format(table, values))
        connection.commit()
        return {"result": "success", "status": "OK"}
    except sqlite3.IntegrityError as ie:
        return {"result": "integrity error, id not unique", "status": "error"}

    return result


def update(table, id = None, **values):
    try:
        if id is not None:
            query_string = "UPDATE {} SET ".format(table) + " "
            for key, value in values.items():
                query_string += key + " = " + value + ", " 
            query_string = query_string[0:-2] + " "
            query_string += " WHERE {}_id = {}".format(table,id)
            print(query_string)
            cursor.execute(query_string)
            connection.commit()
            return {"result": "success", "status": "OK"}
        else:
            return {"result": "must send id to update", "status": "error"}
    except sqlite3.OperationalError as oe:
        return {"result": "error, no such column or syntax error", "status": "error"} 


def delete():
    pass