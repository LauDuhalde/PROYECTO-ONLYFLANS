# Generated by Django 4.2 on 2024-04-16 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_contactformmodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactFormModel',
            new_name='ContactForm',
        ),
    ]