# Generated by Django 3.2 on 2022-03-02 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avaliacao',
            old_name='avaliacoes',
            new_name='avaliacao',
        ),
    ]