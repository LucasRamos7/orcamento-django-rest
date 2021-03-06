# Generated by Django 4.0.1 on 2022-01-28 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=20)),
                ('data', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=20)),
                ('data', models.DateField()),
            ],
        ),
    ]
