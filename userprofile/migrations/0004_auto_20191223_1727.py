# Generated by Django 2.2.9 on 2019-12-23 09:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20160728_1139'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ['id'], 'verbose_name': '用户信息', 'verbose_name_plural': '用户信息'},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='lang',
            field=models.CharField(default='en_US', max_length=5, verbose_name='语言'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='student_id',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='学生编号'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]