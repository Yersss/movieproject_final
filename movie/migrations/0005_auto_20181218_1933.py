# Generated by Django 2.1.4 on 2018-12-18 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_auto_20181218_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genres',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]
