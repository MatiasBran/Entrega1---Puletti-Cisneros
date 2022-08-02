# Generated by Django 4.0.6 on 2022-07-31 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('subtitulo', models.CharField(max_length=50)),
                ('contenido', models.TextField(null=True)),
                ('autor', models.CharField(max_length=50)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('fecha', models.DateField(null=True)),
            ],
        ),
    ]
