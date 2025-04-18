# Generated by Django 4.2.20 on 2025-03-20 07:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_customuser_managers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_activity',
            name='login_time',
        ),
        migrations.RemoveField(
            model_name='user_activity',
            name='logout_time',
        ),
        migrations.AddField(
            model_name='user_activity',
            name='last_login_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user_activity',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
