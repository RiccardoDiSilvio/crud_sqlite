import sqlite3

def create(table, **values):
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()
    tuple_values = []
    for key, item in values.items():
        tuple_values.append(item)

    tuple_values = str(tuple(tuple_values))
    print(tuple_values)
    try:
        print("INSERT into {} VALUES {}".format(table, tuple_values))
        cursor.execute("INSERT into {} VALUES {}".format(table, tuple_values))
        connection.commit()
        return {"result": "success", "status": "OK"}
    except sqlite3.IntegrityError as ie:
        return {"result": "integrity error, id not unique", "status": "error"}

    return result


def update(table, id, **values):
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()
    print("values", values)
    try:
        query_string = ""
        for key, item in values.items():
            print(key, item)
            query_string += key + " = "
            query_string += item if type(item).__name__ != 'str' else "'" + item + "'"
            query_string += ", "
        
        query_string = query_string[0:-2]
        query_string = "UPDATE {} SET {} WHERE {}_id = {}".format(table, query_string, table, id)
        print(query_string)
        cursor.execute(query_string)
        connection.commit()
        return {"result": "success", "status": "OK"}
    except sqlite3.OperationalError as oe:
        return {"result": "error, no such column or syntax error", "status": "error"} 


def delete(table, id):
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE from {} where {}_id = {}".format(table, table, id))
        connection.commit()
        return {"result": "success", "status": "OK"}
    except sqlite3.OperationalError as oe:
        return {"result": "error, no such column or syntax error", "status": "error"} 


