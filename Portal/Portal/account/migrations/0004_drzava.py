# Generated by Django 3.2.7 on 2021-09-25 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_volonter_cv'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drzava',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=200)),
            ],
        ),
    ]
