# Generated by Django 3.1.4 on 2020-12-26 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starbucks', '0007_auto_20201226_0548'),
    ]

    operations = [
        migrations.AddField(
            model_name='allergy',
            name='drinks',
            field=models.ManyToManyField(to='starbucks.Drinks'),
        ),
        migrations.DeleteModel(
            name='allergy_drink',
        ),
    ]
