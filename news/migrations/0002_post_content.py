# Generated by Django 3.2 on 2021-12-11 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
