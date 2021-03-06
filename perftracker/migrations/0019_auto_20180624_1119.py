# Generated by Django 2.0.3 on 2018-06-24 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perftracker', '0018_auto_20180624_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='hwfarmnodemodel',
            name='cpu_score_smp',
            field=models.FloatField(blank=True, help_text='1.01', null=True),
        ),
        migrations.AddField(
            model_name='hwfarmnodemodel',
            name='disk_score_smp',
            field=models.FloatField(blank=True, help_text='0.92', null=True),
        ),
        migrations.AddField(
            model_name='hwfarmnodemodel',
            name='network_score_smp',
            field=models.FloatField(blank=True, help_text='1.21', null=True),
        ),
        migrations.AddField(
            model_name='hwfarmnodemodel',
            name='ram_score_smp',
            field=models.FloatField(blank=True, help_text='1.85', null=True),
        ),
        migrations.AddField(
            model_name='hwfarmnodemodel',
            name='storage_flush_per_sec_smp',
            field=models.IntegerField(blank=True, help_text='20124', null=True),
        ),
    ]
