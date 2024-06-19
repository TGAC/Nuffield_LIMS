from django.shortcuts import render
from django.http import HttpResponse
from .models import Sample, Extraction, QC, Sequencing

# Create your views here.
def index(request):
    samples = Sample.objects.all()
    context = {"samples": samples}
    return render(request, 'index.html', context)

def sample_detail(request, sample_id):
    detail = Sample.objects.get(pk=sample_id)
    extractions = detail.extraction_set.all()
    context = {"sample": detail, "extractions": extractions}
    return render(request, 'sample_detail.html', context)

def sample_extraction(request, extraction_id):
    extraction = Extraction.objects.get(pk=extraction_id)
    qcs = extraction.qc_set.all()
    sequencing = extraction.sequencing_set.all()
    sample = extraction.sample
    context = {"extraction": extraction, "qcs": qcs, "sequencing": sequencing, "sample": sample}
    return render(request, 'sample_extraction.html', context)

