# Generated by Django 3.2.5 on 2021-07-09 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Writers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('writer_uid', models.CharField(max_length=4)),
                ('mobile', models.CharField(max_length=10)),
                ('experience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='writer_register.experience')),
            ],
        ),
    ]
