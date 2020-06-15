# Generated by Django 3.0.7 on 2020-06-12 19:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('materialsearch', '0006_material_publish_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='publish_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
