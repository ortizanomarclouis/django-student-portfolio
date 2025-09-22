from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"

class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField(help_text="Skill level in percentage (0-100)")
    
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Education(models.Model):
    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    current = models.BooleanField(default=False, help_text="Currently studying here")
    
    def __str__(self):
        return f"{self.degree} at {self.school}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} - {self.subject}"