# Generated by Django 3.1 on 2020-08-24 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shortener', '0002_shortlyurl_shortcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortlyurl',
            name='shortcode',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]