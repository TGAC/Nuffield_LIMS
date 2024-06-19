from django.shortcuts import render
from django.http import HttpResponse
from .models import Sample, Extraction, QC, Sequencing

# Create your views here.
def index(request):
    """
    This view function handles the request for the index page of the application.

    Parameters:
    request (HttpRequest): A Django HttpRequest object representing the incoming HTTP request.

    Returns:
    HttpResponse: A Django HttpResponse object that renders the 'index.html' template with the context data.
    """

    # Query all Sample objects from the database
    samples = Sample.objects.all()

    # Prepare the context data for the template. The context is a dictionary where
    # the key is the name of the variable in the template, and the value is the actual value you want to pass in.
    context = {"samples": samples}

    # Render the 'index.html' template with the given context data and return the HttpResponse object
    return render(request, 'index.html', context)

def sample_detail(request, sample_id):
    """
    This view function handles the request for the detail page of a specific sample.

    Parameters:
    request (HttpRequest): A Django HttpRequest object representing the incoming HTTP request.
    sample_id (int): The ID of the sample to display.

    Returns:
    HttpResponse: A Django HttpResponse object that renders the 'sample_detail.html' template with the context data.
    """

    # Get the Sample object with the given ID from the database
    detail = Sample.objects.get(pk=sample_id)

    # Query all Extraction objects related to the Sample object from the database
    extractions = detail.extraction_set.all()

    # Prepare the context data for the template. The context is a dictionary where
    # the key is the name of the variable in the template, and the value is the actual value you want to pass in.
    context = {"sample": detail, "extractions": extractions}

    # Render the 'sample_detail.html' template with the given context data and return the HttpResponse object
    return render(request, 'sample_detail.html', context)
def sample_extraction(request, extraction_id):
    """
    This view function handles the request for the detail page of a specific extraction.

    Parameters:
    request (HttpRequest): A Django HttpRequest object representing the incoming HTTP request.
    extraction_id (int): The ID of the extraction to display.

    Returns:
    HttpResponse: A Django HttpResponse object that renders the 'sample_extraction.html' template with the context data.
    """

    # Get the Extraction object with the given ID from the database
    extraction = Extraction.objects.get(pk=extraction_id)

    # Query all QC objects related to the Extraction object from the database
    qcs = extraction.qc_set.all()

    # Query all Sequencing objects related to the Extraction object from the database
    sequencing = extraction.sequencing_set.all()

    # Get the Sample object related to the Extraction object from the database
    sample = extraction.sample

    # Prepare the context data for the template. The context is a dictionary where
    # the key is the name of the variable in the template, and the value is the actual value you want to pass in.
    context = {"extraction": extraction, "qcs": qcs, "sequencing": sequencing, "sample": sample}

    # Render the 'sample_extraction.html' template with the given context data and return the HttpResponse object
    return render(request, 'sample_extraction.html', context)