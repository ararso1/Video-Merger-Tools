# Generated by Django 4.0.3 on 2022-12-16 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merger_tools', '0008_cut_merged_remove_cut_original_cut_merded_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cut_original',
            name='cut_original',
        ),
        migrations.AddField(
            model_name='cut_original',
            name='v',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]
