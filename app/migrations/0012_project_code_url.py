# Generated by Django 4.2.4 on 2023-09-02 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_tool'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='code_url',
            field=models.TextField(blank=True, null=True),
        ),
    ]
