import sqlite3

def getPrimaryKey(table):
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()
    result = cursor.execute("PRAGMA table_info({})".format(table))
    primary_key = ""
    for line in result:
        if line[5] == 1:
            primary_key = line[1]
    return primary_key

def create(table, **values):
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()
    tuple_keys = []
    tuple_values = []
    for key, item in values.items():
        tuple_keys.append(key)
        print(item)
        if type(item).__name__ == 'int':
            print("es un enetro")
            tuple_values.append(item)
        elif item == "" or item == "null":
            print("es vacio")
            tuple_values.append("null")
        else:
            print("es un string")
            tuple_values.append(item) 

    tuple_keys = str(tuple(tuple_keys))
    tuple_values = str(tuple(tuple_values))
    print(tuple_values)
    try:
        print("INSERT into {} {} VALUES {}".format(table, tuple_keys, tuple_values))
        cursor.execute("INSERT into {} {} VALUES {}".format(table, tuple_keys, tuple_values).replace("'null'", "null"))
        connection.commit()
        return {"result": "success", "status": "OK"}
    except sqlite3.IntegrityError as ie:
        return {"result": "integrity error, id not unique", "status": "error"}

    return result


def update(table, id, **values):
    print(values, "update")
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()
    print("values", values)
    try:
        for key, item in values.items():
            if item == "":
                continue

            if type(item).__name__ == 'str':
                item = "'" + item + "'"
                

            query_string = "UPDATE {} SET {} = {} WHERE {} = {}".format(table, key, item, getPrimaryKey(table), id)
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
        cursor.execute("DELETE from {} where {} = {}".format(table, getPrimaryKey(table), id))
        connection.commit()
        return {"result": "success", "status": "OK"}
    except sqlite3.OperationalError as oe:
        return {"result": "error, no such column or syntax error", "status": "error"} 


