# Generated by Django 5.0.3 on 2024-03-10 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locais', '0004_remove_corredor_loes_id_remove_corredor_sles_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corredor',
            name='coes_dsc',
            field=models.CharField(db_column='COES_DSC', max_length=100, unique=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='posicao',
            name='poes_dsc',
            field=models.CharField(db_column='POES_DSC', max_length=100, unique=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='prateleira',
            name='pres_dsc',
            field=models.CharField(db_column='PRES_DSC', max_length=100, unique=True, verbose_name='Descrição'),
        ),
    ]