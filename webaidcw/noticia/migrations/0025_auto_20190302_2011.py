# Generated by Django 2.1.5 on 2019-03-02 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0024_auto_20190302_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='albumimagen',
            name='imagen',
        ),
        migrations.AddField(
            model_name='albumimagen',
            name='imagen1',
            field=models.ImageField(blank=True, null=True, upload_to='Noticia/album', verbose_name='Imagen principal'),
        ),
        migrations.AddField(
            model_name='albumimagen',
            name='imagen2',
            field=models.ImageField(blank=True, null=True, upload_to='Noticia/album', verbose_name='Imagen 2'),
        ),
        migrations.AddField(
            model_name='albumimagen',
            name='imagen3',
            field=models.ImageField(blank=True, null=True, upload_to='Noticia/album', verbose_name='Imagen 3'),
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='album',
        ),
        migrations.AddField(
            model_name='noticia',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='noticia.AlbumImagen'),
        ),
    ]
