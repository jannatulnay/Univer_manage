# Generated by Django 3.2.6 on 2022-05-22 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myversity', '0005_auto_20220522_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='referece_number',
            field=models.CharField(default='1784', max_length=7, unique=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='eventsimg',
            field=models.ImageField(upload_to='departnentimages/'),
        ),
    ]
