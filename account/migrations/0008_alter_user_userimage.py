# Generated by Django 4.0.1 on 2022-01-30 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_user_userimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userImage',
            field=models.ImageField(default=False, null=True, upload_to='users/'),
        ),
    ]
