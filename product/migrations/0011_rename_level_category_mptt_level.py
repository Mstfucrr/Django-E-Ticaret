# Generated by Django 3.2.3 on 2021-08-12 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20210812_1632'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='level',
            new_name='mptt_level',
        ),
    ]
