from rest_framework import viewsets
from .models import Material
from .serializer import MaterialSerializer

class MateriaisViewSet(viewsets.ModelViewSet):
    """EXIBINDO TODOS MATERIAIS"""
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    