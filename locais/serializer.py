from rest_framework import serializers
from .models import Local, SubLocal, Corredor, Prateleira, Posicao, Enderecamento

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = ['loes_id', 'loes_dsc', 'loes_dat_cria', 'user_id', 'loes_dat_atua']

class SubLocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubLocal
        fields = ['loes_id', 'sles_id', 'sles_dsc', 'sles_dat_cria', 'user_id', 'sles_dat_atua']

class CorredorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corredor
        fields = ['coes_id', 'coes_dsc', 'coes_dat_cria', 'user_id', 'coes_dat_atua']

class PrateleiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prateleira
        fields = ['pres_id', 'pres_dsc', 'pres_dat_cria', 'user_id', 'pres_dat_atua']

class PosicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posicao
        fields = ['poes_id', 'poes_dsc', 'poes_dat_cria', 'user_id', 'poes_dat_atua']