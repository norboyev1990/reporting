# Generated by Django 3.0.6 on 2020-06-04 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0009_auto_20200604_1518'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportdata',
            old_name='CODE_CONRACT',
            new_name='CODE_CONTRACT',
        ),
    ]
