# Generated by Django 3.0.7 on 2020-06-12 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materialsearch', '0005_auto_20200610_0050'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='publish_date',
            field=models.DateTimeField(default='2020-06-01 11:00', null=True),
        ),
    ]