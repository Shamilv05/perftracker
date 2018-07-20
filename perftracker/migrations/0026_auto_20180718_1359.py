# Generated by Django 2.0.3 on 2018-07-18 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perftracker', '0025_auto_20180718_1351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hwfarmnodelockmodel',
            name='planned_dur_hrs',
        ),
        migrations.AddField(
            model_name='hwfarmnodelockmodel',
            name='planned_dur_hrs',
            field=models.IntegerField(default=24, help_text='Planned lock duration (hours)'),
            preserve_default=False,
        ),
    ]
