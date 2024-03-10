from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Material, Grupo, ControleMaterial
from .serializer import MaterialSerializer, GrupoSerializer, ControleMaterialSerializer, ListaMateriaisPorGrupoSerializer

class GruposViewSet(viewsets.ModelViewSet):
    """EXIBINDO TODOS GRUPOS"""
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaMateriaisPorGrupo(generics.ListAPIView):
    """LISTANDO TODOS MATERIAIS POR GRUPO"""
    def get_queryset(self):
        queryset = Material.objects.filter(grup_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMateriaisPorGrupoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class MateriaisViewSet(viewsets.ModelViewSet):
    """EXIBINDO TODOS MATERIAIS"""
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class ControleMateriaisViewSet(viewsets.ModelViewSet):
    """EXIBINDO TODOS GRUPOS"""
    queryset = ControleMaterial.objects.all()
    serializer_class = ControleMaterialSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    