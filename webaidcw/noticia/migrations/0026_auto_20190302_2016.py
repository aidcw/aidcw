# Generated by Django 2.1.5 on 2019-03-02 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0025_auto_20190302_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumimagen',
            name='imagen1',
            field=models.ImageField(blank=True, null=True, upload_to='Noticia', verbose_name='Imagen principal'),
        ),
        migrations.AlterField(
            model_name='albumimagen',
            name='imagen2',
            field=models.ImageField(blank=True, null=True, upload_to='Noticia', verbose_name='Imagen 2'),
        ),
        migrations.AlterField(
            model_name='albumimagen',
            name='imagen3',
            field=models.ImageField(blank=True, null=True, upload_to='Noticia', verbose_name='Imagen 3'),
        ),
    ]
