# Generated by Django 4.2.2 on 2023-06-21 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Scheduler', '0003_courses_alter_lectures_course_delete_course'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Instuctor',
            new_name='Instructor',
        ),
        migrations.RenameField(
            model_name='lectures',
            old_name='instuctor',
            new_name='instructor',
        ),
        migrations.AlterField(
            model_name='courses',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
