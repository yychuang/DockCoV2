# Generated by Django 3.0.4 on 2020-04-07 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0005_auto_20200319_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cid2Drugbankid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.IntegerField()),
                ('drugbank_id', models.CharField(max_length=10)),
            ],
        ),
    ]
