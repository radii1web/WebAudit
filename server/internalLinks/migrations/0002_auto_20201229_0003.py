# Generated by Django 3.1.4 on 2020-12-29 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internalLinks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='internallinks',
            name='div',
        ),
        migrations.RemoveField(
            model_name='internallinks',
            name='script',
        ),
        migrations.AddField(
            model_name='internallinks',
            name='result',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
