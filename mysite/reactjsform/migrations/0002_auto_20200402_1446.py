# Generated by Django 3.0.5 on 2020-04-02 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactjsform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
