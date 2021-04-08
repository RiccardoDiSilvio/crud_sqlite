import sqlite3
from django.shortcuts import render
from crudsqlite import settings
from .crud import create, update, delete, consulta1, consulta2, consulta3, consulta4
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

        return render(request, "padre_crud.html", {"padres": list_elements("padre"), "context": context})

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

        return render(request, "hijo_crud.html", {"hijos": list_elements("hijo"), "context": context})

    elif request.method == "GET":
        return render(request, "hijo_crud.html", {"hijo": ""})


def Consulta1View(request):
    if request.method == "POST":
        id = request.POST["id"]
        resultado = consulta1(id)
        print(resultado)
        hijos = []
        for line in resultado:
            hijos.append({"id": line[0], "nombre": line[1]})
        return render(request, "post_consulta1.html", {"hijos": hijos})

    elif request.method == "GET":
        return render(request, "get_consulta1.html", {"padres": list_elements("padre")})

def Consulta2View(request):
    resultado = consulta2()
    print(resultado)
    padres = []
    for line in resultado:
        padres.append({"id": line[0], "nombre": line[1]})
    return render(request, "consulta2.html", {"padres": padres})


def Consulta3View(request):
    resultado = consulta3()
    print(resultado)
    hijos = []
    for line in resultado:
        hijos.append({"id": line[0], "nombre": line[1], "padre_id": line[2]})
    return render(request, "consulta3.html", {"hijos": hijos})


def Consulta4View(request):
    resultado = consulta4()
    padres = []
    for line in resultado:
        padres.append({"id": line[0], "nombre": line[1], "count": line[2]})
    return render(request, "consulta4.html", {"padres": padres})


def MainMenuView(request):
    return render(request, "main.html")


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