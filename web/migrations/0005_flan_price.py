# Generated by Django 4.2 on 2024-04-18 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_rename_contactformmodel_contactform'),
    ]

    operations = [
        migrations.AddField(
            model_name='flan',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
    ]
