# Generated by Django 2.1.5 on 2019-03-02 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0021_auto_20190302_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumImagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('imagen', models.ImageField(upload_to='Noticia/album', verbose_name='Imagen Noticia')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='Fecha modificación')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='noticia.Noticia')),
            ],
            options={
                'verbose_name': 'imagen',
                'verbose_name_plural': 'imagenes',
                'ordering': ['-fecha_creacion'],
            },
        ),
    ]
