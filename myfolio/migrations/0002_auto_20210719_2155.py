# Generated by Django 3.2 on 2021-07-19 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='user_image',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_image',
            field=models.URLField(),
        ),
    ]
