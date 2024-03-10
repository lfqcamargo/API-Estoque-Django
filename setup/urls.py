from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from materiais.views import MateriaisViewSet, GruposViewSet, ControleMateriaisViewSet, ListaMateriaisPorGrupo
# Importe os viewsets dos locais
from locais.views import LocalViewSet, SubLocalViewSet, CorredorViewSet, PrateleiraViewSet, PosicaoViewSet

router = routers.DefaultRouter()
router.register('grupos', GruposViewSet, basename='Grupos')
router.register('materiais', MateriaisViewSet, basename='Materiais')
router.register('controlemateriais', ControleMateriaisViewSet, basename='Controle Materiais')

router.register('locais', LocalViewSet, basename='Locais')
router.register('sublocais', SubLocalViewSet, basename='SubLocais')
router.register('corredores', CorredorViewSet, basename='Corredores')
router.register('prateleiras', PrateleiraViewSet, basename='Prateleiras')
router.register('posicoes', PosicaoViewSet, basename='Posicoes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('grupo/<int:pk>/materiais/', ListaMateriaisPorGrupo.as_view()),
]
