# Generated by Django 3.1.5 on 2021-02-11 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20210210_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='photo',
            field=models.ImageField(default='staff-pics/default.jpg', upload_to='staff-pics'),
        ),
    ]