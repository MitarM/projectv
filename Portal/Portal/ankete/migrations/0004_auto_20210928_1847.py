# Generated by Django 3.2.7 on 2021-09-28 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ankete', '0003_auto_20210926_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='anketa',
            name='autor_ankete',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='anketa',
            name='vidljivost_ankete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pitanja',
            name='anketa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ankete.anketa'),
        ),
        migrations.AddField(
            model_name='stavka',
            name='ispitanik',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Otvorena_pitanja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('odgovor', models.CharField(max_length=300, null=True)),
                ('ispitanik', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pitanje', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ankete.pitanja')),
            ],
        ),
    ]
