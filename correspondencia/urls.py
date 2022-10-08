from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"oficinas", views.OficinaViewSet)
router.register(r"tipos", views.TipoViewSet)
router.register(r"correlativos", views.CorrelativoViewSet)
router.register(r"documentos", views.documentoViewSet)

urlpatterns = [
    #path('', views.index, name='index'),
    path('', include(router.urls))
]