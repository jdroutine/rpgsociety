# Generated by Django 3.2.3 on 2021-07-22 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characterCard', '0010_alter_character_sneaking'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='analisys',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='charm',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='coding',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='conduction',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='conversance',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='diy',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='empathy',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='investigation',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='movement',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='strength',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='understanding',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], null=True),
        ),
    ]
