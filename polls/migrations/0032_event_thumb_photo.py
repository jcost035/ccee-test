# Generated by Django 3.1.5 on 2021-06-11 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0031_auto_20210611_0328'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='thumb_photo',
            field=models.ImageField(blank=True, default='staff-pics/default.jpg', upload_to='programs'),
        ),
    ]