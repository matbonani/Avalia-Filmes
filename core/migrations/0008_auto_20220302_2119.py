# Generated by Django 3.2 on 2022-03-02 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_avaliacao_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='ativo',
            field=models.BooleanField(default=True, verbose_name='Ativo'),
        ),
        migrations.AlterField(
            model_name='filme',
            name='ativo',
            field=models.BooleanField(default=True, verbose_name='Ativo'),
        ),
    ]
