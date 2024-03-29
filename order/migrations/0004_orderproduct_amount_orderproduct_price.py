# Generated by Django 4.0.4 on 2022-06-15 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_orderproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='amount',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='price',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
