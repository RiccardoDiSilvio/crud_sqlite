import sqlite3
from django.shortcuts import render
from crudsqlite import settings
from rest_framework.views import APIView
from .crud import create, update, delete
from .serializers import *
# Create your views here.

class AnimalCrudView(APIView):
    def post(self, request):
        serializer = AnimalSerializer(data = request.data)
        print(request.data)
        if serializer.is_valid():
            data = dict(serializer.validated_data)
            if data["crud_method"] == "CREATE":
                data.pop("crud_method")
                context = create("animal", **data)

            elif data["crud_method"] == "UPDATE":
                data.pop("crud_method")
                print(data)
                if "tipo" in data:
                   create("cambio_de_rol", ternero_id = data["animal_id"], rol_escogido = data["tipo"]) 
                context = update("animal", data["animal_id"], **data)

            elif data["crud_method"] == "DELETE":
                context = delete("animal", id = data["animal_id"])
        else:
            print(serializer.errors)
        return render(request, "index1.html", {"animales": list_elements("animal"), "context": context})

    def get(self, request):
        return render(request, "index1.html", {"animales": list_elements("animal")})


class AlimentacionCrudView(APIView):
    def post(self, request):
        serializer = AlimentacionSerializer(data = request.data)
        if serializer.is_valid():
            data = dict(serializer.validated_data)
            print(data)
            if data["crud_method"] == "CREATE":
                data.pop("crud_method")
                context = create("alimentacion", **data)

            elif data["crud_method"] == "UPDATE":
                data.pop("crud_method")
                context = update("alimentacion", data["alimentacion_id"], **data)

            elif data["crud_method"] == "DELETE":
                context = delete("alimentacion", id = data["alimentacion_id"])

        return render(request, "index7.html", {"alimentaciones": list_elements("alimentacion"), "context": context})

    def get(self, request):
        return render(request, "index7.html", {"alimentaciones": list_elements("alimentacion")})


class CitaDeControlCrudView(APIView):
    def post(self, request):
        serializer = CitaDeControlSerializer(data = request.data)
        if serializer.is_valid():
            data = dict(serializer.validated_data)
            print(data)
            if data["crud_method"] == "CREATE":
                data.pop("crud_method")
                context = create("cita_de_control", **data)

            elif data["crud_method"] == "UPDATE":
                data.pop("crud_method")
                context = update("cita_de_control", data["ins_id"],  **data)

            elif data["crud_method"] == "DELETE":
                context = delete("cita_de_control", id = data["ins_id"])

        return render(request, "index6.html", {"citas": list_elements("cita_de_control"), "context": context})

    def get(self, request):
        return render(request, "index6.html", {"citas": list_elements("cita_de_control")})


class InseminacionCrudView(APIView):
    def post(self, request):
        serializer = InseminacionSerializer(data = request.data)
        if serializer.is_valid():
            data = dict(serializer.validated_data)
            print(data)
            if data["crud_method"] == "CREATE":
                data.pop("crud_method")
                context = create("inseminacion", **data)

            elif data["crud_method"] == "UPDATE":
                data.pop("crud_method")
                context = update("inseminacion", data["ins_id"], **data)

            elif data["crud_method"] == "DELETE":
                context = delete("inseminacion", id = data["ins_id"])

        return render(request, "index5.html", {"inseminaciones": list_elements("inseminacion"), "context": context})

    def get(self, request):
        return render(request, "index5.html", {"inseminaciones": list_elements("inseminacion")})


class PajillaCrudView(APIView):
    def post(self, request):
        serializer = PajillaSerializer(data = request.data)
        if serializer.is_valid():
            data = dict(serializer.validated_data)
            print(data)
            if data["crud_method"] == "CREATE":
                data.pop("crud_method")
                context = create("pajilla", **data)

            elif data["crud_method"] == "UPDATE":
                data.pop("crud_method")
                context = update("pajilla", data["pajilla_id"], **data)

            elif data["crud_method"] == "DELETE":
                context = delete("pajilla", id = data["pajilla_id"])

        return render(request, "index3.html", {"pajillas": list_elements("pajilla"), "context": context})

    def get(self, request):
        return render(request, "index3.html", {"pajillas": list_elements("pajilla")})


class ProcesoVeterinarioCrudView(APIView):
    def post(self, request):
        serializer = ProcesoVeterinarioSerializer(data = request.data)
        if serializer.is_valid():
            data = dict(serializer.validated_data)
            print(data)
            if data["crud_method"] == "CREATE":
                data.pop("crud_method")
                context = create("proceso_veterinario", **data)

            elif data["crud_method"] == "UPDATE":
                data.pop("crud_method")
                context = update("proceso_veterinario", data["proceso_id"], **data)

            elif data["crud_method"] == "DELETE":
                context = delete("proceso_veterinario", id = data["proceso_id"])

        return render(request, "index2.html", {"procesos": list_elements("proceso_veterinario"), "context": context})

    def get(self, request):
        return render(request, "index2.html", {"procesos": list_elements("proceso_veterinario")})


class VentaCrudView(APIView):
    def post(self, request):
        serializer = VentaSerializer(data = request.data)
        if serializer.is_valid():
            data = dict(serializer.validated_data)
            print(data)
            if data["crud_method"] == "CREATE":
                data.pop("crud_method")
                context = create("venta", **data)

            elif data["crud_method"] == "UPDATE":
                data.pop("crud_method")
                context = update("venta", data["venta_id"], **data)

            elif data["crud_method"] == "DELETE":
                context = delete("venta", id = data["venta_id"])

        return render(request, "index.html", {"ventas": list_elements("venta"), "context": context})

    def get(self, request):
        return render(request, "index.html", {"ventas": list_elements("venta")})


class VeterinarioCrudView(APIView):
    def post(self, request):
        serializer = VeterinarioSerializer(data = request.data)
        if serializer.is_valid():
            data = dict(serializer.validated_data)
            print(data)
            if data["crud_method"] == "CREATE":
                data.pop("crud_method")
                context = create("veterinario", **data)

            elif data["crud_method"] == "UPDATE":
                data.pop("crud_method")
                context = update("veterinario", data["vet_id"], **data)

            elif data["crud_method"] == "DELETE":
                context = delete("veterinario", id = data["vet_id"])

        return render(request, "index8.html", {"veterinarios": list_elements("veterinario"), "context": context})

    def get(self, request):
        return render(request, "index8.html", {"veterinarios": list_elements("veterinario")})


def MainMenuView(request):
    return render(request, "index.html")


def list_elements(table):
    con = sqlite3.connect("db.sqlite3")
    cur=con.cursor()
    cur.execute("SELECT * FROM {}".format(table))
    values = []
    for line in cur.fetchall():
        if table == "animal":
            values.append({"animal_id": line[0], "tipo": line[1], "fecha_de_baja": line[2], "motivo_de_baja": line[3]})
        elif table == "alimentacion":
            values.append({"alimentacion_id": line[0], "fecha": line[1], "kilos_consumidos": line[2], "agua_consumida": line[3], "animal_id": line[4]})
        elif table == "cita_de_control":
            values.append({"ins_id": line[0], "fecha": line[1], "diagnostico": line[2]})
        elif table == "inseminacion":
            values.append({"ins_id": line[0], "fecha_inseminacion": line[1], "exitosa": line[2], "peso_inicial": line[3], "vet_id": line[4], "vaca_id": line[5], "pajilla_id": line[6]})
        elif table == "pajilla":
            values.append({"pajilla_id": line[0], "fecha": line[1], "toro_id": line[2]})
        elif table == "proceso_veterinario":
            values.append({"proceso_id": line[0], "fecha": line[1], "tipo": line[2], "tiempo_evolucion": line[3], "nom_enfermedad": line[4], "nom_vacuna": line[5], "vet_id": line[6], "animal_id": line[7]})
        elif table == "venta":
            values.append({"venta_id": line[0], "tipo_venta": line[1], "fecha": line[2], "animal_id": line[3], "pajilla_id": line[4], "peso_en_venta": line[5], "precio": line[6]})
        elif table == "veterinario":
            values.append({"vet_id": line[0], "telefono": line[1], "email": line[2]})
        
    print(table, values)
    return values