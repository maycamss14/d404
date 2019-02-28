# Generated by Django 2.1.7 on 2019-02-28 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('genero', models.CharField(choices=[('ac', 'Ação'), ('av', 'Aventura'), ('cm', 'Comédia'), ('dr', 'Drama'), ('fc', 'Ficção'), ('tr', 'Terror'), ('ro', 'Romance')], default=None, max_length=2)),
                ('sinopse', models.TextField()),
                ('lancamento', models.DateField()),
                ('duracao', models.PositiveIntegerField()),
                ('classificacao_indicativa', models.PositiveIntegerField()),
                ('cartaz', models.ImageField(upload_to='media')),
            ],
        ),
    ]
