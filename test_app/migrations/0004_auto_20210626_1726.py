# Generated by Django 3.2.4 on 2021-06-26 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0003_auto_20210626_1700'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testmodel',
            options={'ordering': ('-created_at',)},
        ),
        migrations.RenameField(
            model_name='testmodel',
            old_name='updates_at',
            new_name='updated_at',
        ),
        migrations.AddField(
            model_name='testmodel',
            name='extra_name',
            field=models.CharField(blank=True, default='null', editable=False, max_length=250, null=True),
        ),
    ]