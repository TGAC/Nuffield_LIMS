from django.db import models
from datetime import datetime
# Create your models here.

class Sample(models.Model):
    taxon_id = models.IntegerField()
    scientific_name = models.CharField(max_length=200)
    common_name = models.CharField(max_length=200)

class Extraction(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)
    extraction_date = models.DateTimeField('date extracted', default=datetime.now())
    extraction_method = models.CharField(max_length=200, default="")
    isPass = models.BooleanField(default=False)

class QC(models.Model):
    extraction = models.ForeignKey(Extraction, on_delete=models.CASCADE)
    qc_date = models.DateTimeField('date qc', default=datetime.now())
    qc_method = models.CharField(max_length=200)
    qc_result = models.BooleanField(default=False)

    def isPass(self):
        return self.qc_result

class Sequencing(models.Model):
    extraction = models.ForeignKey(Extraction, on_delete=models.CASCADE)
    sequencing_date = models.DateTimeField('date sequenced', default=datetime.now())
    sequencing_method = models.CharField(max_length=200, default="")
    sequencing_read_length = models.IntegerField(default=0)

    def isShortRead(self):
        return self.sequencing_read_length < 10000