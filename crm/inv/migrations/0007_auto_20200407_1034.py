# Generated by Django 3.0.5 on 2020-04-07 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0006_auto_20200407_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
