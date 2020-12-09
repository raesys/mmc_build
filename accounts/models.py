from django.db import models
from django.contrib.auth.models import User
# from tinymce import HTMLField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='username')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, verbose_name='your email', help_text='Enter your active email address')
    phone = models.CharField(max_length=15, verbose_name='your phone number')
    interest = models.CharField(max_length=200, verbose_name='your interests')
    code_goal = models.TextField(verbose_name='your coding goal')

    def __str__(self):
        return self.user.username


class Project(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    live_project_link = models.URLField(max_length=200)
    codebase_link = models.URLField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Chat(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    # message = HTMLField('Content Message')
    message = models.TextField()

    def __str__(self):
        return self.subject

