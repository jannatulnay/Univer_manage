# Generated by Django 4.0.5 on 2022-07-01 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myversity', '0015_alter_registration_referece_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='referece_number',
            field=models.CharField(default='7542', max_length=7, unique=True),
        ),
    ]