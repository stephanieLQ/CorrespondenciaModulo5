from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from correspondencia.models import Correlativo, Oficina
from correspondencia.models import Tipo, Documento
from correspondencia.serializers import CorrelativoSerializer, DocumentoSerializer, OficinaSerializer, TipoSerializer

def index(request):
    return HttpResponse("Hola Mundo")

class OficinaViewSet(viewsets.ModelViewSet):
    queryset = Oficina.objects.all()
    serializer_class = OficinaSerializer

class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer

class CorrelativoViewSet(viewsets.ModelViewSet):
    queryset = Correlativo.objects.all()
    serializer_class = CorrelativoSerializer

class documentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer