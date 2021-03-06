# Generated by Django 3.2.7 on 2021-09-18 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diskusija',
            name='vidljivost',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Сви'), (2, 'Волонтери')], default=1),
        ),
        migrations.AlterField(
            model_name='diskusija',
            name='vidljivost_za_org',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Сви'), (2, 'Волонтери'), (3, 'Волонтери истих интересовања')], default=1),
        ),
    ]
