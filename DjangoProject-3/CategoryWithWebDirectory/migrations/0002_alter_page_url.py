# Generated by Django 3.2.1 on 2021-05-27 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.CharField(max_length=50),
        ),
    ]