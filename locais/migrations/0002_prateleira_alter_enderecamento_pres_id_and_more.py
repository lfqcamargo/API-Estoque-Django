# Generated by Django 5.0.3 on 2024-03-10 13:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locais', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Prateleira',
            fields=[
                ('pres_id', models.AutoField(db_column='PRES_ID', primary_key=True, serialize=False, verbose_name='Prateleira')),
                ('pres_dsc', models.CharField(db_column='PRES_DSC', max_length=100, unique=True, verbose_name='Descrição')),
                ('pres_dat_cria', models.DateTimeField(auto_now_add=True, db_column='PRES_DAT_CRIA', verbose_name='Data da Criação')),
                ('pres_dat_atua', models.DateTimeField(auto_now=True, db_column='PRES_DAT_ATUA', verbose_name='Ultima Atualização')),
                ('coes_id', models.ForeignKey(db_column='COES_ID', on_delete=django.db.models.deletion.CASCADE, to='locais.corredor', verbose_name='Corredor')),
                ('loes_id', models.ForeignKey(db_column='LOES_ID', on_delete=django.db.models.deletion.CASCADE, to='locais.local', verbose_name='Local')),
                ('sles_id', models.ForeignKey(db_column='SLES_ID', on_delete=django.db.models.deletion.CASCADE, to='locais.sublocal', verbose_name='Sub-Local')),
                ('user_id', models.ForeignKey(db_column='USER_ID', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Pratileira',
                'verbose_name_plural': 'Pratileiras',
                'db_table': 'PRES',
            },
        ),
        migrations.AlterField(
            model_name='enderecamento',
            name='pres_id',
            field=models.ForeignKey(db_column='PRES_ID', on_delete=django.db.models.deletion.CASCADE, to='locais.prateleira', verbose_name='Prateleira'),
        ),
        migrations.AlterField(
            model_name='posicao',
            name='pres_id',
            field=models.ForeignKey(db_column='PRES_ID', on_delete=django.db.models.deletion.CASCADE, to='locais.prateleira', verbose_name='Prateleira'),
        ),
        migrations.DeleteModel(
            name='Pratileira',
        ),
    ]