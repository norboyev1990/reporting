# Generated by Django 3.0.6 on 2020-06-04 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0003_listreports_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listreports',
            name='DATE_CREATED',
            field=models.DateTimeField(null=True),
        ),
    ]
