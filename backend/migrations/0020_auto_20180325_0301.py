# Generated by Django 2.0.2 on 2018-03-25 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0019_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(to='backend.Category'),
        ),
    ]