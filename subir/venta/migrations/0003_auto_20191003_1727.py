# Generated by Django 2.2.4 on 2019-10-03 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0002_auto_20191003_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle_venta',
            name='canti',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Cantidad'),
        ),
    ]