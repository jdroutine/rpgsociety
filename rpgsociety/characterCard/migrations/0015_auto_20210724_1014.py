# Generated by Django 3.2.3 on 2021-07-24 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characterCard', '0014_auto_20210724_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='status1',
            field=models.CharField(choices=[('Brak', 'None'), ('Zdenerwowanie', 'Nervousness'), ('Przerażenie', 'Horror'), ('Zmęczenie', 'Fatigue'), ('Zranienie', 'Injury'), ('Wycieńczenie', 'Weakness')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='status2',
            field=models.CharField(choices=[('Brak', 'None'), ('Zdenerwowanie', 'Nervousness'), ('Przerażenie', 'Horror'), ('Zmęczenie', 'Fatigue'), ('Zranienie', 'Injury'), ('Wycieńczenie', 'Weakness')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='status3',
            field=models.CharField(choices=[('Brak', 'None'), ('Zdenerwowanie', 'Nervousness'), ('Przerażenie', 'Horror'), ('Zmęczenie', 'Fatigue'), ('Zranienie', 'Injury'), ('Wycieńczenie', 'Weakness')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='status4',
            field=models.CharField(choices=[('Brak', 'None'), ('Zdenerwowanie', 'Nervousness'), ('Przerażenie', 'Horror'), ('Zmęczenie', 'Fatigue'), ('Zranienie', 'Injury'), ('Wycieńczenie', 'Weakness')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='status5',
            field=models.CharField(choices=[('Brak', 'None'), ('Zdenerwowanie', 'Nervousness'), ('Przerażenie', 'Horror'), ('Zmęczenie', 'Fatigue'), ('Zranienie', 'Injury'), ('Wycieńczenie', 'Weakness')], max_length=50, null=True),
        ),
    ]
