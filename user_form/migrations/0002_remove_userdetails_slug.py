# Generated by Django 4.1.6 on 2023-02-13 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_form', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='slug',
        ),
    ]
