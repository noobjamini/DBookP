from django.shortcuts import render

# Create your views here.
from catalog.models import Applicant

def index(request):
    return render(request, 'index.html')

def introduce(request):
    return render(request, 'introduce.html')

def apply(request):
    return render(request, 'apply.html')
