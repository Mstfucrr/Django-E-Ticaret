# Generated by Django 4.0 on 2022-03-01 14:42

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_auto_20210824_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title'),
        ),
    ]
