# Generated by Django 4.2.13 on 2024-06-17 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Extraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extraction_date', models.DateTimeField(verbose_name='date extracted')),
                ('extraction_method', models.CharField(max_length=200)),
                ('isPass', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='QC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qc_date', models.DateTimeField(verbose_name='date qc')),
                ('qc_method', models.CharField(max_length=200)),
                ('qc_result', models.CharField(max_length=200)),
                ('extraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lims_core.extraction')),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxon_id', models.IntegerField()),
                ('scientific_name', models.CharField(max_length=200)),
                ('common_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sequencing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequencing_date', models.DateTimeField(verbose_name='date sequenced')),
                ('sequencing_method', models.CharField(max_length=200)),
                ('sequencing_read_length', models.CharField(max_length=200)),
                ('qc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lims_core.qc')),
            ],
        ),
        migrations.AddField(
            model_name='extraction',
            name='sample',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lims_core.sample'),
        ),
    ]
