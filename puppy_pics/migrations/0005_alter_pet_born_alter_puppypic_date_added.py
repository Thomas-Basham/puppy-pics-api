# Generated by Django 4.0.5 on 2022-07-12 00:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('puppy_pics', '0004_alter_puppypic_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='born',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='puppypic',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 12, 0, 42, 57, 98533, tzinfo=utc)),
        ),
    ]
