# Generated by Django 4.0.5 on 2022-06-03 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('puppy_pics', '0004_remove_puppypic_img_url_puppypic_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='puppypic',
            old_name='image',
            new_name='img',
        ),
    ]