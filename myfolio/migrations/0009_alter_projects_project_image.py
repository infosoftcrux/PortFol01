# Generated by Django 3.2.5 on 2021-10-07 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfolio', '0008_alter_otpreset_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='project_image',
            field=models.URLField(blank=True),
        ),
    ]
