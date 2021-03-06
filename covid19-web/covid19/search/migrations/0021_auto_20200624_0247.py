# Generated by Django 3.0.4 on 2020-06-24 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0020_auto_20200612_0757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drugsimilarity',
            name='drug1',
        ),
        migrations.RemoveField(
            model_name='drugsimilarity',
            name='drug2',
        ),
        migrations.AddField(
            model_name='drugsimilarity',
            name='drug1_cid',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='drugsimilarity',
            name='drug2_cid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='drugsimilarity',
            name='dice_similarity_score',
            field=models.FloatField(default=0),
        ),
    ]
