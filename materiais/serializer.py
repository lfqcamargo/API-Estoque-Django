from rest_framework import serializers
from .models import Material

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Material
        fields = ['mate_id', 'mate_dsc', 'mate_dat_cria', 'mate_user', 'mate_dat_atua']