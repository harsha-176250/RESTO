# Generated by Django 2.1.7 on 2019-04-07 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('offer_id', models.IntegerField(default=1, primary_key=True, serialize=False)),
            ],
        ),
    ]
