# Generated by Django 3.2.4 on 2021-06-26 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_auto_20210626_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='updates_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
