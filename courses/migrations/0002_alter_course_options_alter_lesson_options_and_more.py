# Generated by Django 4.2.16 on 2024-12-02 08:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-created_at'], 'verbose_name': 'Course', 'verbose_name_plural': 'Courses'},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['order'], 'verbose_name': 'Lesson', 'verbose_name_plural': 'Lessons'},
        ),
        migrations.AlterModelOptions(
            name='userrole',
            options={'verbose_name': 'User Role', 'verbose_name_plural': 'User Roles'},
        ),
        migrations.AlterField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Timestamp when the course was created.'),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(help_text='Detailed description of the course.'),
        ),
        migrations.AlterField(
            model_name='course',
            name='is_published',
            field=models.BooleanField(default=False, help_text='Indicates whether the course is published.'),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(help_text='Title of the course.', max_length=255),
        ),
        migrations.AlterField(
            model_name='course',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Timestamp when the course was last updated.'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='content',
            field=models.TextField(help_text='Content of the lesson.'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(help_text='The course to which the lesson belongs.', on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='courses.course'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='order',
            field=models.PositiveIntegerField(help_text='Order of the lesson within the course.'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='title',
            field=models.CharField(help_text='Title of the lesson.', max_length=255),
        ),
        migrations.AlterField(
            model_name='userrole',
            name='course',
            field=models.ForeignKey(help_text='The course for which the role is assigned.', on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='courses.course'),
        ),
        migrations.AlterField(
            model_name='userrole',
            name='date_assigned',
            field=models.DateTimeField(auto_now_add=True, help_text='Timestamp when the role was assigned.'),
        ),
        migrations.AlterField(
            model_name='userrole',
            name='role',
            field=models.CharField(choices=[('student', 'Student'), ('instructor', 'Instructor')], help_text='Role of the user in the course.', max_length=20),
        ),
        migrations.AlterField(
            model_name='userrole',
            name='user',
            field=models.ForeignKey(help_text='The user assigned a role.', on_delete=django.db.models.deletion.CASCADE, related_name='roles', to=settings.AUTH_USER_MODEL),
        ),
    ]
