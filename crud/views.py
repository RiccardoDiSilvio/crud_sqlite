import sqlite3
from django.shortcuts import render
from crudsqlite import settings
from .crud import create, update, delete
# Create your views here.
def PadreCrudView(request):
    if request.method == "POST":
        if request.POST["id"] == '':
            return render(request, "padre_crud.html", {"padres": "", "message": "Necesita mandar id para hacer operacion"})

        id = int(request.POST["id"])
        if request.POST["crud-method"] == "CREATE":
            context = create("padre", id = id, nom = request.POST["nombre"] if request.POST["nombre"] != '' else 'null')

        if request.POST["crud-method"] == "UPDATE":
            context = update("padre", id = id, nom = request.POST["nombre"] if request.POST["nombre"] != '' else 'null')

        if request.POST["crud-method"] == "DELETE":
            context = delete("padre", id = id)

        return render(request, "padre_crud.html", {"padres": list_elements("padre")})

    elif request.method == "GET":
        return render(request, "padre_crud.html", {"padres": list_elements("padre")})


def HijoCrudView(request):
    if request.method == "POST":
        print(request.POST)
        if request.POST["id"] == '':
            return render(request, "hijo_crud.html", {"hijos": "", "message": "Necesita mandar id para hacer operacion"})

        id = int(request.POST["id"])
        if request.POST["crud-method"] == "CREATE":
            context = create("hijo", id = id, nom = request.POST["nombre"] if request.POST["nombre"] != '' else 'null', padre_id = request.POST["hijode"] if request.POST["hijode"] != '' else 'null')

        if request.POST["crud-method"] == "UPDATE":
            context = update("hijo", id = id, nom = request.POST["nombre"] if request.POST["nombre"] != '' else 'null', padre_id = request.POST["hijode"] if request.POST["hijode"] != '' else 'null')

        if request.POST["crud-method"] == "DELETE":
            context = delete("hijo", id = id)

        return render(request, "hijo_crud.html", {"hijos": list_elements("hijo")})

    elif request.method == "GET":
        return render(request, "hijo_crud.html", {"hijo": ""})

def list_elements(table):
    con = sqlite3.connect("db.sqlite3")
    cur=con.cursor()
    cur.execute("SELECT * FROM {}".format(table))
    values = []
    for line in cur.fetchall():
        if table == "padre":
            values.append({"id": line[0], "nombre": line[1]})
        elif table == "hijo":
            values.append({"id": line[0], "nombre": line[1], "hijode": line[2]})
    print(table, values)
    return values