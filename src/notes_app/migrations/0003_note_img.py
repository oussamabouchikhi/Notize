# Generated by Django 3.0.2 on 2020-01-08 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0002_auto_20200108_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='img',
            field=models.ImageField(default='', upload_to='notes-img'),
            preserve_default=False,
        ),
    ]
