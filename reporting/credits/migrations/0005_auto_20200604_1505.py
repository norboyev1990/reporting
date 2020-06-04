# Generated by Django 3.0.6 on 2020-06-04 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0004_auto_20200604_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportdata',
            name='REPORT',
        ),
        migrations.AddField(
            model_name='reportdata',
            name='REPORT_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='REPORT_ID', to='credits.ListReports'),
        ),
    ]
