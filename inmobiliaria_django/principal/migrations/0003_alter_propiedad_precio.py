# Generated by Django 5.2.1 on 2025-05-13 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_propiedad_numero_recamaras_propiedad_tipo_compra_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=18),
        ),
    ]
