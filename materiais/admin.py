from django.contrib import admin
from .models import Material

class Materiais(admin.ModelAdmin):
    list_display = ['mate_id', 'mate_dsc', 'mate_dat_cria', 'mate_user', 'mate_dat_atua']
    list_display_links = ('mate_id', 'mate_dsc')
    search_fields = ('mate_dsc',)
    list_per_page = 20

admin.site.register(Material, Materiais)