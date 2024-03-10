from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Local, SubLocal, Corredor, Prateleira, Posicao
from .serializer import LocalSerializer, SubLocalSerializer, CorredorSerializer, PrateleiraSerializer, PosicaoSerializer

class LocalViewSet(viewsets.ModelViewSet):
    """EXIBINDO TODOS LOCAIS"""
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['loes_dsc']
    ordering_fields = ['loes_dsc']

    queryset = Local.objects.all()
    serializer_class = LocalSerializer

class SubLocalViewSet(viewsets.ModelViewSet):
    """EXIBINDO TODOS SUBLOCAIS"""
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['sles_dsc']
    ordering_fields = ['sles_dsc']

    queryset = SubLocal.objects.all()
    serializer_class = SubLocalSerializer

class CorredorViewSet(viewsets.ModelViewSet):
    """EXIBINDO TODOS CORREDORES"""
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['coes_dsc']
    ordering_fields = ['coes_dsc']

    queryset = Corredor.objects.all()
    serializer_class = CorredorSerializer

class PrateleiraViewSet(viewsets.ModelViewSet):
    """EXIBINDO TODAS PRATELEIRAS"""
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['pres_dsc']
    ordering_fields = ['pres_dsc']

    queryset = Prateleira.objects.all()
    serializer_class = PrateleiraSerializer

class PosicaoViewSet(viewsets.ModelViewSet):
    """EXIBINDO TODAS POSIÇÕES"""
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['poes_dsc']
    ordering_fields = ['poes_dsc']

    queryset = Posicao.objects.all()
    serializer_class = PosicaoSerializer
