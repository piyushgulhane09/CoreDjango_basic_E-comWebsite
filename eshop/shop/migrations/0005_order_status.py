# Generated by Django 4.1.7 on 2023-04-25 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
