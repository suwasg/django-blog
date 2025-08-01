# Generated by Django 5.2.4 on 2025-07-23 08:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('img', models.FileField(blank=True, null=True, upload_to='category/')),
                ('description', models.TextField()),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('img', models.FileField(blank=True, null=True, upload_to='blog/')),
                ('description', models.TextField()),
                ('sort_description', models.TextField()),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('is_slider', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
                ('tag', models.ManyToManyField(to='blog.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField()),
                ('rating', models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3, max_length=100)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
            ],
        ),
    ]
