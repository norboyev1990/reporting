# Generated by Django 3.0.7 on 2020-07-18 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0003_problemcredits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempdata2',
            name='NAME_CLIENT',
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]
