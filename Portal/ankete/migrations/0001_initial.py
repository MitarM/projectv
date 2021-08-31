# Generated by Django 3.2.6 on 2021-08-29 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pitanja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tekst', models.CharField(max_length=200)),
                ('datum', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Stavka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tekst', models.CharField(max_length=60)),
                ('glasovi', models.IntegerField()),
                ('pitanje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ankete.pitanja')),
            ],
        ),
    ]
