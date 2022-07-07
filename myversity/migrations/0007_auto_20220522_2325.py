# Generated by Django 3.2.6 on 2022-05-22 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myversity', '0006_auto_20220522_2213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deparetment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_code', models.CharField(max_length=100)),
                ('dep_name', models.CharField(max_length=240)),
            ],
        ),
        migrations.AlterField(
            model_name='registration',
            name='referece_number',
            field=models.CharField(default='2390', max_length=7, unique=True),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=100)),
                ('course_name', models.CharField(max_length=240)),
                ('credit', models.IntegerField()),
                ('description', models.TextField()),
                ('semister', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], default='1', max_length=50)),
                ('deparetment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myversity.deparetment')),
            ],
        ),
    ]
