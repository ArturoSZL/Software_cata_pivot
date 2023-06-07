# Generated by Django 3.1.3 on 2023-06-06 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alimentos',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('catadores', models.PositiveSmallIntegerField()),
                ('descripcion', models.TextField()),
            ],
        ),
    ]
