# Generated by Django 3.0.7 on 2020-07-13 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0015_auto_20200708_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='ByAverageUl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255, verbose_name='Срок')),
                ('AverageUZS', models.FloatField(verbose_name='UZS')),
                ('AverageUSD', models.FloatField(verbose_name='USD')),
                ('AverageEUR', models.FloatField(verbose_name='EUR')),
                ('AverageJPY', models.FloatField(verbose_name='JPY')),
                ('TotalUZS', models.FloatField()),
                ('TotalUSD', models.FloatField()),
                ('TotalEUR', models.FloatField()),
                ('TotalJPY', models.FloatField()),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ByOverdueBranch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255, verbose_name='Филиал')),
                ('Balance', models.FloatField(verbose_name='Выданные')),
                ('Overdue', models.FloatField(verbose_name='Просрочка')),
                ('CountPr', models.FloatField(verbose_name='Количество')),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ByAverageFl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255, verbose_name='Продукты')),
                ('Balance', models.FloatField(verbose_name='UZS')),
                ('Average', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TempData2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CODE_REG', models.CharField(max_length=255)),
                ('MFO', models.CharField(max_length=255)),
                ('NAME_CLIENT', models.CharField(max_length=255)),
                ('SUMMA_CREDIT', models.CharField(max_length=255)),
                ('DATE_VIDACHI', models.CharField(max_length=255)),
                ('OSTATOK_NACH_PRCNT', models.CharField(max_length=255)),
                ('KREDIT_SCHET', models.CharField(max_length=255)),
                ('OSTATOK_SCHETA', models.CharField(max_length=255)),
                ('DATE_POGASH', models.CharField(max_length=255)),
                ('SUMMA_POGASH', models.CharField(max_length=255)),
                ('PROGNOZ_POGASH', models.CharField(max_length=255)),
                ('SCHET_PROSR', models.CharField(max_length=255)),
                ('OSTATOK_PROSR', models.CharField(max_length=255)),
                ('CODE_VAL', models.CharField(max_length=255)),
                ('VID_KREDITOVANIYA', models.CharField(max_length=255)),
                ('ISTOCHNIK_KREDIT', models.CharField(max_length=255)),
                ('UNIQUE_NIKI', models.CharField(max_length=255)),
                ('MONTH_CODE', models.IntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='databygeocode',
            name='id',
        ),
        migrations.AlterField(
            model_name='databygeocode',
            name='GeoCode',
            field=models.CharField(max_length=7, primary_key=True, serialize=False),
        ),
    ]