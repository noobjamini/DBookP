# Generated by Django 5.1.4 on 2025-01-03 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('major', models.CharField(choices=[('설계', '첨단로봇설계과'), ('제어', '첨단로봇제어과'), ('시스템', '첨단로봇소프트웨어과'), ('군특', '첨단로봇정보통신과')], max_length=3)),
                ('gender', models.CharField(choices=[('M', '남자'), ('F', '여자'), ('O', '기타')], max_length=1)),
                ('phone_number', models.CharField(help_text='"-"기호 없이 입력', max_length=15)),
                ('motivation', models.TextField()),
                ('aspirations', models.TextField(blank=True, null=True)),
                ('favorite_book', models.CharField(blank=True, help_text='좋아하는 책 한 권만 입력', max_length=100, null=True)),
            ],
        ),
    ]
