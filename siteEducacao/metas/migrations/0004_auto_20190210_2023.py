# Generated by Django 2.1.5 on 2019-02-10 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metas', '0003_auto_20190210_2020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indicador',
            old_name='nao_executado',
            new_name='não_executado',
        ),
        migrations.RenameField(
            model_name='metas',
            old_name='meta_description',
            new_name='Descrição_da_meta',
        ),
        migrations.RenameField(
            model_name='metas',
            old_name='numero_meta',
            new_name='número_da_meta',
        ),
    ]
