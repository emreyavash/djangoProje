# Generated by Django 4.0 on 2022-01-29 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='userImage',
            field=models.ImageField(default=False, upload_to='uploads'),
        ),
    ]
