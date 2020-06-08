# Generated by Django 3.0.7 on 2020-06-08 00:47

from django.db import migrations, models
import django.db.models.deletion
import materialsearch.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('material_type', models.CharField(choices=[('LuctuerNotes', 'LuctuerNotes'), ('Exam form', 'Exam form'), ('Worcksheet', 'Worcksheet'), ('Book', 'Book'), ('Syllabus', 'Syllabus')], max_length=60)),
                ('year', models.PositiveIntegerField(default=materialsearch.models.current_year)),
                ('semester', models.CharField(choices=[('first semester', 'first semester'), ('second semester', 'second semester'), ('summer semester', 'summer semester')], max_length=20)),
                ('link', models.URLField(max_length=500)),
                ('dumy', models.BooleanField(default=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='materialsearch.Course')),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='materialsearch.Doctor')),
            ],
        ),
    ]
