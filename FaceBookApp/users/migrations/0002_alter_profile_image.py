# Generated by Django 4.2.2 on 2023-06-28 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics/<django.db.models.query_utils.DeferredAttribute object at 0x000002A667845100>'),
        ),
    ]