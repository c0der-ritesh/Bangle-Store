# Generated by Django 5.0.4 on 2024-05-07 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=30)),
                ('pdesc', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=9)),
            ],
        ),
    ]
