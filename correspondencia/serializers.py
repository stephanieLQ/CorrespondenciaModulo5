from rest_framework import serializers
from .models import Oficina
from .models import Tipo
from .models import Correlativo
from .models import Documento

class OficinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oficina
        fields = "__all__"

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = "__all__"

class CorrelativoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Correlativo
        fields = "__all__"

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = "__all__"