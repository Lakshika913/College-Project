# Generated by Django 3.2.4 on 2021-07-01 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp_portal', '0009_teacher_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_image'),
        ),
    ]