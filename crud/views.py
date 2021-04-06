import sqlite3
from django.shortcuts import render
from crudsqlite import settings
from .crud import create, update, delete
# Create your views here.
def PadreCrudView(request):
    if request.method == "POST":
        # operation = request.POST["operation"]
        # table = request.POST["table"]
        # arguments = request.POST["arguments"]
        if request.POST["crud-method"] == "CREATE":
            context = create("padre", "(" + request.POST["id"] + ", '" + request.POST["nombre"] + "')")
        elif request.POST["crud-method"] == "UPDATE":
            context = update("padre", id = request.POST["id"], nom = "'" + request.POST["nombre"] + "'")
        print(context)
        context["padres"] = list_elements("padre")
        return render(request, "padre_crud.html", context)

    elif request.method == "GET":
        return render(request, "padre_crud.html", {"padres": list_elements("padre")})


def list_elements(table):
    con = sqlite3.connect("db.sqlite3")
    cur=con.cursor()
    cur.execute("SELECT * FROM {}").format(table)
    padres = []
    for line in cur:
        print(line)
        padres.append({"id": line[0], "nombre": line[1]})
    print(padres)
    return padres