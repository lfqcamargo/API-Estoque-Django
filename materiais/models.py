from django.db import models
from django.conf import settings

class Material(models.Model):
    mate_id = models.AutoField(primary_key=True, db_column='MATE_ID', verbose_name='ID')
    mate_dsc = models.CharField(max_length=100, null=False, blank=False, db_column='MATE_DSC', verbose_name='Descrição')
    mate_dat_cria = models.DateTimeField(auto_now_add=True, null=False, blank=False, db_column='MATE_DAT_CRIA', verbose_name='Data da Criação')
    mate_user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, db_column='MATE_USR', verbose_name='Usuário')
    mate_dat_atua = models.DateTimeField(auto_now=True, null=False, blank=False, db_column='MATE_DAT_ATUA', verbose_name='Ultima Atualização')

    def __str__(self):
        return self.mate_dsc
    
    class Meta():
        db_table = 'MATE'
        verbose_name = 'Material'
        verbose_name_plural = 'Materiais'