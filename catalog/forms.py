from django import forms

from catalog.models import Applicant

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ("student_id", "name", "major", "gender", "phone_number", "motivation", "aspirations", "favorite_book")
        labels = {
            'student_id': '학번',
            'name': '이름',
            'major': '전공(과)',
            'gender': '성별',
            'phone_number': '전화번호',
            'motivation': '지원 동기',
            'aspirations': '각오 및 포부',
            'favorite_book': '좋아하는 책',
        }
        