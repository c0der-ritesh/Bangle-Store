# Generated by Django 5.0.4 on 2024-05-09 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_orderdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='Date',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
