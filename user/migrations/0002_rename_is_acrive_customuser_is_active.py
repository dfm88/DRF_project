# Generated by Django 3.2.4 on 2021-07-21 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='is_acrive',
            new_name='is_active',
        ),
    ]
