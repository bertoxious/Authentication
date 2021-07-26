from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
# Create your models here.


class BasicDetails(models.Model):
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    users = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    father_name = models.CharField(max_length=50, blank=True, null=True)
    mother_name = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDERS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name+" "+ self.last_name


class Education(BasicDetails):
    current_year = datetime.date.today().year
    YEAR_CHOICES = [(r, r) for r in range(2000, datetime.date.today().year+2)]
    course_name = models.CharField(max_length=100, blank=True, null=True)
    university_board_name = models.CharField(
        max_length=200, blank=True, null=True)
    passing_year = models.IntegerField(
        choices=YEAR_CHOICES, default=current_year, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=timezone.now)

    

