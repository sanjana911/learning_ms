from django.db import models
from accounts.models import User

# Create your models here.

class TrainerProfile(models.Model):

    name = models.CharField(max_length=100)

    department = models.CharField(max_length=200)

    experience = models.CharField(max_length=100)

    profile_picture = models.ImageField(upload_to="profile_pitcure", null=True)

    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="trainer_profile")


class StudentProfile(models.Model):

    name = models.CharField(max_length=100)

    skills = models.CharField(max_length=200, null=True)

    pass_out_year = models.PositiveIntegerField()

    profile_picture = models.ImageField(upload_to="profile_pictures", null= True)

    created_at = models.DateTimeField(auto_now_add=True)

    created_by = models.OneToOneField(User,on_delete=models.CASCADE, related_name="student_profile")