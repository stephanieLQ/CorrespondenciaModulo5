from django.contrib import admin
from .models import Oficina
from .models import Tipo
from .models import Correlativo
from .models import Documento

class OficinaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "sigla", "estado")
    ordering = ["nombre"]
    search_fields = ["nombre"]
    list_filter = ("estado",)

admin.site.register(Oficina, OficinaAdmin)

class TipoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "abreviatura", "cite", "estado")
    ordering = ["nombre"]
    search_fields = ["nombre"]
    list_filter = ("estado",)
    
admin.site.register(Tipo, TipoAdmin)

class CorrelativoAdmin(admin.ModelAdmin):
    list_display = ("oficina", "tipo", "correlativo", "gestion")
    ordering = ["oficina"]
    search_fields = ["oficina"]
    list_filter = ("gestion",)
    
admin.site.register(Correlativo, CorrelativoAdmin)

class DocumentoAdmin(admin.ModelAdmin):
    list_display = ("oficina", "tipo", "cite", "referencia","usaurio","estado")
    ordering = ["oficina"]
    search_fields = ["oficina"]
    list_filter = ("usaurio",)
    
admin.site.register(Documento, DocumentoAdmin)