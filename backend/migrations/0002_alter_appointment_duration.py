# Generated by Django 4.0.dev20210827112741 on 2021-12-03 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='duration',
            field=models.IntegerField(),
        ),
    ]
