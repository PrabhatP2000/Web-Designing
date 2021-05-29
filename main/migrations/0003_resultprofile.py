# Generated by Django 3.2.3 on 2021-05-28 18:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_delete_resultprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SEM', models.IntegerField()),
                ('SUBJECT_NAME1', models.CharField(max_length=100)),
                ('SUBJECT_NAME2', models.CharField(max_length=100)),
                ('SUBJECT_NAME3', models.CharField(max_length=100)),
                ('SUBJECT_NAME4', models.CharField(max_length=100)),
                ('SUBJECT_NAME5', models.CharField(max_length=100)),
                ('MARK1', models.IntegerField()),
                ('MARK2', models.IntegerField()),
                ('MARK3', models.IntegerField()),
                ('MARK4', models.IntegerField()),
                ('MARK5', models.IntegerField()),
                ('BRANCH', models.CharField(max_length=60)),
                ('ROLL_NO', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
