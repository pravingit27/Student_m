# Generated by Django 4.0 on 2021-12-30 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vertos', '0005_alter_class_details_major_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('designation', models.CharField(max_length=50)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='vertos.user')),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='vertos.user')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_school', to='vertos.school')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_name', to='vertos.user')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='vertos.user')),
            ],
            options={
                'verbose_name': 'staff',
                'verbose_name_plural': 'staffs',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=30)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='vertos.user')),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='vertos.user')),
                ('subject_major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='vertos.major')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='vertos.user')),
            ],
            options={
                'verbose_name': 'subject',
                'verbose_name_plural': 'subjects',
            },
        ),
        migrations.CreateModel(
            name='Staff_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('class_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_class', to='vertos.class_details')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='vertos.user')),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='vertos.user')),
                ('staff_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_detail', to='vertos.staff')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_subject', to='vertos.subject')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='vertos.user')),
            ],
            options={
                'verbose_name': 'staff-detail',
                'verbose_name_plural': 'staff-details',
            },
        ),
    ]
