# Generated by Django 3.2.4 on 2021-07-01 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp_portal', '0010_student_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='qualification',
            field=models.CharField(default='B.Tech', max_length=20),
        ),
    ]
