# Generated by Django 4.0.1 on 2022-02-06 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_remove_courses_teacher_courses_teacher'),
        ('shoppingCard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopping',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='category.teacher'),
        ),
    ]
