# Generated by Django 3.1.4 on 2020-12-26 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starbucks', '0010_allergy_drinks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allergy',
            name='drinks',
        ),
        migrations.AddField(
            model_name='drinks',
            name='allergy',
            field=models.ManyToManyField(to='starbucks.Allergy'),
        ),
    ]
