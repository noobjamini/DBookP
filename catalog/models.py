from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.
class Applicant(models.Model):
    STUDENT_ID_MAX_LENGTH = 10
    GENDER_CHOICES = [
        ('M', '남자'),
        ('F', '여자'),
        ('O', '기타'),
    ]
    MAJOR_CHOICES = [
        ('설계', '첨단로봇설계과'),
        ('제어', '첨단로봇제어과'),
        ('시스템', '첨단로봇소프트웨어과'),
        ('군특', '첨단로봇정보통신과'),
    ]

    student_id = models.CharField(max_length=STUDENT_ID_MAX_LENGTH, unique=True)
    name = models.CharField(max_length=50)
    major = models.CharField(max_length=3, choices=MAJOR_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(help_text = '"-"기호 없이 입력', max_length=15)
    motivation = models.TextField() # 지원 동기
    aspirations = models.TextField(blank=True, null=True) # 포부
    favorite_book = models.CharField(help_text = '좋아하는 책 한 권만 입력', max_length=100, blank=True, null=True) # 

    def __str__(self):
        return f"{self.name} ({self.student_id})"