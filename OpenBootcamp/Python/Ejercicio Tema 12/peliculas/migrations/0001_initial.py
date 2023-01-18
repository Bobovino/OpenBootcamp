# Generated by Django 4.1.2 on 2022-10-27 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Pon el nombre del autor.', max_length=64)),
                ('apellidos', models.CharField(help_text='Pon los apellidos del autor.', max_length=64)),
                ('numero_oscars', models.PositiveIntegerField()),
                ('biografia', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Pon el nombre de la película.', max_length=64)),
                ('fecha_estreno', models.PositiveIntegerField()),
                ('duracion', models.PositiveIntegerField()),
                ('sinopsis', models.TextField()),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peliculas.director')),
            ],
        ),
    ]
