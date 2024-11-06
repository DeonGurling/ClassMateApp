from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.

# database for Educators / Advisors
class Educators(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='educator', default='')
    name = models.CharField(max_length=200, default='')
    surname = models.CharField(max_length=200, default='')
    phone = models.CharField(max_length=200, default='')
    address = models.CharField(max_length=200, default='')
    profile_pic = models.ImageField(upload_to='educator_profile_pic/', blank=False, default='')

    class Meta:
        verbose_name_plural = "Educators"

    def __str__(self):
        return self.name + ', ' + self.surname



# Database for students/learners

class Students(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student', default='')
    name = models.CharField(max_length=200, default='')
    surname = models.CharField(max_length=200, default='')
    phone = models.CharField(max_length=200, default='')
    address = models.CharField(max_length=200, default='')
    profile_pic = models.ImageField(upload_to='student_profile_pic/', blank=False, default='')

    class Meta:
        verbose_name_plural = "Students"

    def __str__(self):
        return self.name + ', ' + self.surname

class Assignments(models.Model):
    title = models.CharField(max_length=100)
    advisor = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='assignments/pdfs/')

    class Meta:
        verbose_name_plural = 'Assignments'

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)