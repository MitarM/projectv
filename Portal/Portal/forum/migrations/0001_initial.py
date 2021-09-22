# Generated by Django 3.2.7 on 2021-09-18 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Diskusija',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=100)),
                ('tekst', models.TextField()),
                ('datum', models.DateTimeField(auto_now_add=True)),
                ('vidljivost', models.PositiveSmallIntegerField(default=1)),
                ('vidljivost_za_org', models.PositiveSmallIntegerField(choices=[(1, 'Svi'), (2, 'Volonteri'), (3, 'Volonteri istih interesovanja')], default=1)),
                ('autor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Kategorija_diskusije',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Komentar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sadrzaj', models.TextField()),
                ('datum', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('diskusija', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.diskusija')),
            ],
        ),
        migrations.AddField(
            model_name='diskusija',
            name='kategorija',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.kategorija_diskusije'),
        ),
    ]
