# Generated by Django 2.2 on 2020-03-19 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pupil',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='static/pupils/'),
        ),
    ]
