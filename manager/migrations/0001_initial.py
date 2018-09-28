# Generated by Django 2.1.1 on 2018-09-28 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blocktopusid', models.IntegerField()),
                ('token', models.CharField(max_length=10)),
                ('public_address', models.CharField(max_length=200)),
                ('verto_address', models.CharField(max_length=200)),
                ('kyc_date', models.DateTimeField(verbose_name='date published')),
                ('whitelist_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
