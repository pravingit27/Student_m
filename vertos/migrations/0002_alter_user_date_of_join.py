# Generated by Django 4.0 on 2022-01-28 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vertos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_join',
            field=models.DateField(blank=True, null=True),
        ),
    ]