# Generated by Django 3.2 on 2021-07-20 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfolio', '0003_alter_about_user_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='user_Experience',
            field=models.CharField(max_length=50),
        ),
    ]
