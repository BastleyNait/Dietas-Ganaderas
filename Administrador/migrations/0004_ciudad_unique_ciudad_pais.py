# Generated by Django 5.0.6 on 2024-07-06 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador', '0003_alimento_alitipcod_alimento_magcod_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='ciudad',
            constraint=models.UniqueConstraint(fields=('CiuCod', 'PaiCod'), name='unique_ciudad_pais'),
        ),
    ]