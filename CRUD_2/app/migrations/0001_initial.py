# Generated by Django 3.2.18 on 2023-06-15 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank='false', max_length=100, null='false')),
                ('email', models.EmailField(blank='false', max_length=254, null='false')),
                ('age', models.IntegerField(blank='false', null='false')),
                ('gender', models.CharField(max_length=50)),
            ],
        ),
    ]
