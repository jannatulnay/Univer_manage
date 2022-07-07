# Generated by Django 4.0.5 on 2022-06-23 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myversity', '0013_alter_registration_referece_number'),
        ('teacherapp', '0003_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='SemisterRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacherapp.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myversity.loginsite')),
            ],
        ),
    ]
