# Generated by Django 4.0.5 on 2022-07-10 19:56

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('puppy_pics', '0002_pet_puppypic_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='puppypic',
            name='pet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='puppy_pics.pet'),
        ),
        migrations.AlterField(
            model_name='puppypic',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 10, 19, 56, 45, 830213, tzinfo=utc)),
        ),
    ]
