# Generated by Django 4.2.2 on 2023-06-22 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Scheduler', '0005_instructors_alter_lectures_instructor_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Instructors',
            new_name='Instructor',
        ),
        migrations.RenameField(
            model_name='instructor',
            old_name='password',
            new_name='password1',
        ),
    ]
