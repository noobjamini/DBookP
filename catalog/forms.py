from django import forms

from catalog.models import Applicant

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ("student_id", "name", "major", "gender", "phone_number", "motivation", "aspirations", "favorite_book")
        