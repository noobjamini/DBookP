from django.shortcuts import render, redirect

# Create your views here.
from catalog.models import Applicant
from catalog.forms import ApplicantForm

def index(request):
    return render(request, 'index.html')

def introduce(request):
    return render(request, 'introduce.html')

def survey_complete(request):
    return render(request, 'survey_complete.html')

def apply_form(request):
    if request.method == "POST":
        form = ApplicantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('survey_complete')
    else:
        form = ApplicantForm()
    return render(request, 'apply_form.html', {'form': form})

def application_list(request):
    applications = Applicant.objects.all()
    return render(request, 'application_list.html', {'applications': applications})