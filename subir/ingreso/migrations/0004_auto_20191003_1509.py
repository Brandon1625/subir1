# Generated by Django 2.2.4 on 2019-10-03 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ingreso', '0003_auto_20190907_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle_ingreso',
            name='id_prod',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='producto.Producto'),
        ),
    ]
