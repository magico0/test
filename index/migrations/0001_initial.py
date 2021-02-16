# Generated by Django 3.1.6 on 2021-02-15 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import index.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('img', models.ImageField(blank=True, null=True, upload_to=index.models.get_upload_path, verbose_name='Skill Photo')),
                ('desc', models.CharField(blank=True, max_length=300, null=True, verbose_name='Description')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=50, null=True, verbose_name='category name')),
                ('project_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='project name')),
                ('img', models.ImageField(blank=True, null=True, upload_to=index.models.get_upload_path_project, verbose_name='project Photo')),
                ('desc', models.CharField(max_length=300, verbose_name='Description')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=index.models.get_upload_path_user, verbose_name='CV')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main', models.BooleanField(default=False, verbose_name='main')),
                ('bold_title1', models.CharField(blank=True, max_length=50, null=True, verbose_name='Bold Title 1')),
                ('bold_title2', models.CharField(blank=True, max_length=50, null=True, verbose_name='Bold Title 2')),
                ('bold_title3', models.CharField(blank=True, max_length=50, null=True, verbose_name='Bold Title 3')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('img', models.ImageField(blank=True, null=True, upload_to=index.models.get_upload_path, verbose_name='Backgroung Photo')),
                ('desc', models.CharField(max_length=300, verbose_name='Description')),
                ('green_button_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='green button name')),
                ('green_button', models.URLField(blank=True, max_length=500, null=True, verbose_name='green button')),
                ('orange_button_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='orange button name')),
                ('orange_button', models.URLField(blank=True, max_length=500, null=True, verbose_name='orange button')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
