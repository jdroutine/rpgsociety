# Generated by Django 3.2.3 on 2021-07-03 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characterCard', '0004_character'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='luck',
            field=models.IntegerField(null=True),
        ),
    ]
