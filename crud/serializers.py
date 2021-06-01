from rest_framework import serializers

class AlimentacionSerializer(serializers.Serializer):
    crud_method = serializers.CharField(max_length = 100)
    alimentacion_id = serializers.IntegerField(required = False)
    fecha = serializers.CharField(max_length = 100, required = False)
    kilos_consumidos = serializers.IntegerField(required = False)
    agua_consumida = serializers.IntegerField(required = False)
    animal_id = serializers.IntegerField(required = False)


class AnimalSerializer(serializers.Serializer):
    crud_method = serializers.CharField(max_length = 100)
    animal_id = serializers.IntegerField(required = False)
    tipo = serializers.IntegerField(required = False)
    fecha_de_baja = serializers.CharField(max_length = 100, required = False)
    motivo_de_baja = serializers.CharField(max_length = 100, required = False)


class CitaDeControlSerializer(serializers.Serializer):
    crud_method = serializers.CharField(max_length = 100)
    ins_id = serializers.IntegerField(required = False)
    fecha = serializers.CharField(max_length = 100, required = False)
    diagnostico = serializers.CharField(max_length = 100)


class InseminacionSerializer(serializers.Serializer):
    crud_method = serializers.CharField(max_length = 100)
    ins_id = serializers.IntegerField(required = False)
    fecha_inseminacion = serializers.CharField(max_length = 100,required = False)
    exitosa = serializers.BooleanField(required = False)
    peso_inicial = serializers.IntegerField(required = False)
    vet_id = serializers.IntegerField(required = False)
    vaca_id = serializers.IntegerField(required = False)
    pajilla_id = serializers.IntegerField(required = False)


class PajillaSerializer(serializers.Serializer):
    crud_method = serializers.CharField(max_length = 100)
    pajilla_id = serializers.IntegerField(required = False)
    fecha = serializers.CharField(max_length = 100, required = False)
    toro_id = serializers.IntegerField(required = False)


class ProcesoVeterinarioSerializer(serializers.Serializer):
    crud_method = serializers.CharField(max_length = 100)
    proceso_id = serializers.IntegerField(required = False)
    fecha = serializers.CharField(max_length = 100, required = False)
    tipo = serializers.IntegerField(required = False)
    tiempo_evolucion = serializers.IntegerField(required = False)
    nom_enfermedad = serializers.CharField(max_length = 100, required = False)
    nom_vacuna = serializers.CharField(max_length = 100, required = False)
    vet_id = serializers.IntegerField(required = False)
    animal_id = serializers.IntegerField(required = False)


class VentaSerializer(serializers.Serializer):
    crud_method = serializers.CharField(max_length = 100)
    venta_id = serializers.IntegerField(required = False)
    tipo_venta = serializers.IntegerField(required = False)
    fecha = serializers.CharField(max_length = 100, required = False)
    animal_id = serializers.IntegerField(required = False)
    pajilla_id = serializers.IntegerField(required = False)
    peso_en_venta = serializers.IntegerField(required = False)
    precio = serializers.IntegerField(required = False)


class VeterinarioSerializer(serializers.Serializer):
    crud_method = serializers.CharField(max_length = 100)
    vet_id = serializers.IntegerField(required = False)
    telefono = serializers.IntegerField(required = False)
    email = serializers.CharField(max_length = 100, required = False)