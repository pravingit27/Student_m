# Generated by Django 4.0 on 2022-01-03 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vertos', '0007_teaching_staff_details_delete_staff_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('total', models.IntegerField(default=500)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
                'verbose_name': 'exam',
                'verbose_name_plural': 'exams',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('marks', models.FloatField()),
                ('grade', models.CharField(choices=[('O', 'O'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('P', 'P'), ('F', 'F')], default='O', max_length=15)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='vertos.user')),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='vertos.user')),
                ('exam_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam_results', to='vertos.exam')),
                ('student_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_results', to='vertos.student')),
                ('subject_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_results', to='vertos.subject')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='vertos.user')),
            ],
            options={
                'verbose_name': 'result',
                'verbose_name_plural': 'results',
            },
        ),
        migrations.CreateModel(
            name='Exam_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('category_name', models.CharField(max_length=200)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='vertos.user')),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='vertos.user')),
                ('parent_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='vertos.exam_category')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='vertos.user')),
            ],
            options={
                'verbose_name': 'exam_category',
                'verbose_name_plural': 'exam_categories',
            },
        ),
        migrations.AddField(
            model_name='exam',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exams', to='vertos.exam_category'),
        ),
        migrations.AddField(
            model_name='exam',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='vertos.user'),
        ),
        migrations.AddField(
            model_name='exam',
            name='deleted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='vertos.user'),
        ),
        migrations.AddField(
            model_name='exam',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exams', to='vertos.school'),
        ),
        migrations.AddField(
            model_name='exam',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='vertos.user'),
        ),
    ]
