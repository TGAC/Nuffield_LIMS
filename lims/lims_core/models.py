from django.db import models

# Create your models here.

class Sample(models.Model):
    taxon_id = models.IntegerField()
    scientific_name = models.CharField(max_length=200)
    common_name = models.CharField(max_length=200)

class Extraction(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)
    extraction_date = models.DateTimeField('date extracted')
    extraction_method = models.CharField(max_length=200)
    isPass = models.BooleanField()

class QC(models.Model):
    extraction = models.ForeignKey(Extraction, on_delete=models.CASCADE)
    qc_date = models.DateTimeField('date qc')
    qc_method = models.CharField(max_length=200)
    qc_result = models.CharField(max_length=200)

class Sequencing(models.Model):
    qc = models.ForeignKey(QC, on_delete=models.CASCADE)
    sequencing_date = models.DateTimeField('date sequenced')
    sequencing_method = models.CharField(max_length=200)
    sequencing_read_length = models.CharField(max_length=200)