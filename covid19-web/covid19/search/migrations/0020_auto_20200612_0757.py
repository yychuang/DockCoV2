# Generated by Django 3.0.4 on 2020-06-12 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0019_auto_20200525_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelatedDocuments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.IntegerField(db_index=True)),
                ('titles', models.TextField()),
                ('urls', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='druginfo',
            name='active_fragments',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='druginfo',
            name='canonical_smiles',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='druginfo',
            name='chembl4303805_activities',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='druginfo',
            name='chembl4303810_activities',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='druginfo',
            name='chembl4303819_activities',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='druginfo',
            name='chembl_id',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='druginfo',
            name='chembl_smiles',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='druginfo',
            name='clinical_phase',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='druginfo',
            name='disease_area',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='druginfo',
            name='drugbank_smiles',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='druginfo',
            name='formula',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='druginfo',
            name='inchi',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='druginfo',
            name='inchikey',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='druginfo',
            name='indication',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='druginfo',
            name='kegg_compound_id',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='druginfo',
            name='kegg_drug_id',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='druginfo',
            name='moa',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='druginfo',
            name='mol_logp',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='druginfo',
            name='mol_weight',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='druginfo',
            name='num_active_fragments',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='druginfo',
            name='num_hacceptors',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='druginfo',
            name='num_hdonors',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='druginfo',
            name='pert_iname',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='druginfo',
            name='smiles',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='druginfo',
            name='target',
            field=models.TextField(default=''),
        ),
    ]