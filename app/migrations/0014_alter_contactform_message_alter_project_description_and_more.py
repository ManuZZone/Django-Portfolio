# Generated by Django 4.2.4 on 2023-09-03 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_setting_github_url_setting_instagram_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='message',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='setting',
            name='about',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='setting',
            name='contact_description',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='setting',
            name='footer_description',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='setting',
            name='hero_description',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='setting',
            name='kwown_me',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='setting',
            name='project_description',
            field=models.CharField(max_length=512),
        ),
        migrations.DeleteModel(
            name='ExternalLink',
        ),
    ]
