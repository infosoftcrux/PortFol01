# Generated by Django 3.2 on 2021-07-12 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='Titles_you_want_to_show_in_animated_text_and_each_seprate_by_comma',
            new_name='Titles_you_want_to_show_in_animated_text_and_each_seprate_by_comma_and_oneSpace',
        ),
        migrations.AlterField(
            model_name='about',
            name='user_cv_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='user_id',
            field=models.CharField(max_length=18, unique=True),
        ),
    ]