# Generated by Django 4.2.1 on 2023-05-28 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_post_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='images',
            new_name='image',
        ),
    ]