# Generated by Django 3.1.5 on 2021-05-25 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_dailydose'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoseArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1200)),
                ('dates', models.JSONField()),
                ('logo_path', models.CharField(max_length=200)),
                ('about', models.CharField(max_length=1200)),
                ('testimonial', models.CharField(max_length=1200)),
                ('video_path', models.CharField(max_length=200)),
                ('faq', models.JSONField()),
            ],
        ),
    ]
