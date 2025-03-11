from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.
from django.db import models

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
        ('시스템', '첨단로봇시스템과/소프트웨어과'),
        ('군특', '첨단로봇정보통신과'),
    ]

    student_id = models.CharField(
        max_length=STUDENT_ID_MAX_LENGTH,
        unique=True,
        verbose_name="학번"
    )
    name = models.CharField(max_length=50, verbose_name="이름")
    major = models.CharField(max_length=3, choices=MAJOR_CHOICES, verbose_name="학과")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="성별")
    phone_number = models.CharField(
        max_length=15,
        help_text='"-"기호 없이 입력',
        verbose_name="전화번호"
    )
    motivation = models.TextField(verbose_name="지원 동기")
    aspirations = models.TextField(
        blank=True, 
        null=True,
        verbose_name="포부"
    )
    favorite_book = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="좋아하는 책 한 권만 입력",
        verbose_name="좋아하는 책"
    )

    def __str__(self):
        return f"{self.name} ({self.student_id})"
