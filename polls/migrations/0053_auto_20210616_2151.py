# Generated by Django 3.1.5 on 2021-06-17 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0052_auto_20210616_2147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='tags',
            new_name='audience',
        ),
    ]