from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from materiais.views import MateriaisViewSet, GruposViewSet, ControleMateriaisViewSet, ListaMateriaisPorGrupo

router = routers.DefaultRouter()
router.register('grupos', GruposViewSet, basename='Grupos')
router.register('materiais', MateriaisViewSet, basename='Materiais')
router.register('controlemateriais', ControleMateriaisViewSet, basename='Controle Materiais')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('grupo/<int:pk>/materiais/', ListaMateriaisPorGrupo.as_view())
]
