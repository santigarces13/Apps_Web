# Generated by Django 2.2.4 on 2019-09-08 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_materiales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='ficha_tecnica',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='nombre_articulo',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='valor',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
