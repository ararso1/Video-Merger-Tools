# Generated by Django 4.0.3 on 2022-12-16 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merger_tools', '0004_scale'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scale',
            old_name='on_by_many',
            new_name='on_with_many',
        ),
        migrations.RenameField(
            model_name='scale',
            old_name='on_by_one',
            new_name='on_with_one',
        ),
    ]
