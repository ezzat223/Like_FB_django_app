# Generated by Django 4.2.2 on 2023-06-28 06:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 28, 9, 39, 53, 434876)),
        ),
    ]
