# Generated by Django 3.2 on 2022-03-02 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_avaliacoes_avaliacao_avaliacao'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='avaliacao',
            unique_together={('email', 'filme')},
        ),
    ]
