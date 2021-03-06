# Generated by Django 3.2 on 2021-12-11 13:02

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('sub_headline', models.TextField()),
                ('news_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('excerpt', models.TextField(blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_posts', to=settings.AUTH_USER_MODEL)),
                ('downvotes', models.ManyToManyField(blank=True, related_name='downvoted', to=settings.AUTH_USER_MODEL)),
                ('upvotes', models.ManyToManyField(blank=True, related_name='upvoted', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('comment_downvote', models.ManyToManyField(blank=True, related_name='comment_downvoted', to=settings.AUTH_USER_MODEL)),
                ('comment_upvote', models.ManyToManyField(blank=True, related_name='comment_upvoted', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='news.post')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
