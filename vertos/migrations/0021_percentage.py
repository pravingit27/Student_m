# Generated by Django 4.0.1 on 2022-01-17 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vertos', '0020_delete_percentage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Percentage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distinct_percentage', models.IntegerField(blank=True, null=True)),
                ('firstclass_percentage', models.IntegerField(blank=True, null=True)),
                ('pass_percentage', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
