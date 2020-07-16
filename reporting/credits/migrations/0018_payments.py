# Generated by Django 3.0.7 on 2020-07-13 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0017_auto_20200713_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CODE_REG', models.CharField(max_length=25)),
                ('MFO', models.CharField(max_length=5)),
                ('NAME_CLIENT', models.CharField(max_length=255)),
                ('SUMMA_CREDIT', models.FloatField(null=True)),
                ('DATE_VIDACHI', models.DateField(null=True)),
                ('OSTATOK_NACH_PRCNT', models.FloatField(null=True)),
                ('KREDIT_SCHET', models.CharField(max_length=20)),
                ('OSTATOK_SCHETA', models.FloatField(null=True)),
                ('DATE_POGASH', models.DateField(null=True)),
                ('SUMMA_POGASH', models.FloatField(null=True)),
                ('PROGNOZ_POGASH', models.FloatField(null=True)),
                ('SCHET_PROSR', models.CharField(max_length=25)),
                ('OSTATOK_PROSR', models.FloatField(null=True)),
                ('CODE_VAL', models.CharField(max_length=25)),
                ('VID_KREDITOVANIYA', models.CharField(max_length=255)),
                ('ISTOCHNIK_KREDIT', models.CharField(max_length=255)),
                ('UNIQUE_NIKI', models.CharField(max_length=25)),
                ('MONTH_CODE', models.IntegerField(null=True)),
            ],
        ),
    ]