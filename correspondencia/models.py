from django.db import models
from django.conf import settings
from .validators import validar_cite, validar_correlativo, validar_gestion

class Oficina(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    sigla = models.CharField(max_length=50, unique=True)
    estado = models.BooleanField(blank=True, default=True)

    def __str__(self):
            return self.nombre

class Tipo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    abreviatura = models.CharField(max_length=50, unique=True)
    cite = models.CharField(max_length=100, unique=True)
    estado = models.BooleanField(blank=True, default=True)

    def __str__(self):
            return self.nombre

class Correlativo(models.Model):
    oficina   = models.ForeignKey(Oficina, on_delete=models.CASCADE)
    tipo   = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    correlativo = models.IntegerField(default=0, validators=[validar_correlativo,])
    gestion = models.IntegerField(default=0, validators=[validar_gestion,])

class EstadoDocumento(models.TextChoices):
    HABILITADO = 'habilitado', 'Habilitado'
    ANULADO = 'anulado', 'Anulado'

class NurDocumento(models.TextChoices):
    EXTERNO = 'externo', 'E-MDPyEP'
    INTERNO = 'interno', 'MDPyEP'

class Documento(models.Model):
    nur = models.CharField(
        max_length=10,
        choices=NurDocumento.choices,
        default=NurDocumento.EXTERNO
    )
    oficina   = models.ForeignKey(Oficina, on_delete=models.CASCADE)
    tipo   = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    cite = models.CharField(max_length=100, unique=True, validators=[validar_cite,])
    referencia = models.TextField()
    usaurio = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="documento_usuario"
    )
    estado = models.CharField(
        max_length=10,
        choices=EstadoDocumento.choices,
        default=EstadoDocumento.HABILITADO
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)