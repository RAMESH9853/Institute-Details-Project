from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    fee = models.IntegerField()
    duration = models.CharField(max_length=100)
    start_date = models.DateTimeField(max_length=100)
    trainer_name = models.CharField(max_length=100)
    trainer_exp = models.CharField(max_length=100)
    training_mode = models.CharField(max_length=100)

class ContactForm(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.BigIntegerField()
    course = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

class feedbackData(models.Model):
    content = models.TextField(max_length=500)
    date = models.DateTimeField()
    user_name = models.CharField(max_length=100,default='admin')
    