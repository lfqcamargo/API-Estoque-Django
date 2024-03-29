# Generated by Django 5.0.3 on 2024-03-24 10:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locais', '0001_initial'),
        ('materiais', '0010_alter_controlematerial_user_id_alter_grupo_user_id_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LocalMaterial',
            fields=[
                ('loma_id', models.AutoField(db_column='LOMA_ID', primary_key=True, serialize=False, verbose_name='Local do Material')),
                ('loma_dat_cria', models.DateTimeField(auto_now_add=True, db_column='LOMA_DAT_CRIA', verbose_name='Data da Criação')),
                ('loma_dat_atua', models.DateTimeField(auto_now=True, db_column='LOMA_DAT_ATUA', verbose_name='Ultima Atualização')),
                ('ense_id', models.ForeignKey(db_column='ENSE_ID', on_delete=django.db.models.deletion.CASCADE, to='locais.enderecamento', verbose_name='Endereçamento')),
                ('mate_id', models.ForeignKey(db_column='MATE_ID', on_delete=django.db.models.deletion.CASCADE, to='materiais.material', verbose_name='Material')),
                ('user_id', models.ForeignKey(db_column='USER_ID', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Local Mateiral',
                'verbose_name_plural': 'Locais Materiais',
                'db_table': 'LOMA',
                'unique_together': {('ense_id', 'mate_id')},
            },
        ),
    ]
