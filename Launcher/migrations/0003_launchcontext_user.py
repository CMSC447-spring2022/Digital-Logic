# Generated by Django 4.0.3 on 2022-05-06 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Launcher', '0002_errorcontext_launchcontext_delete_choice_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='launchcontext',
            name='user',
            field=models.TextField(blank=True),
        ),
    ]