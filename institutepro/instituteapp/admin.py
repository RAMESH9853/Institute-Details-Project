from django.contrib import admin
from .models import Course

class AdminCourse(admin.ModelAdmin):
    list_display = ['course_name','fee','duration','start_date','trainer_name','trainer_exp','training_mode']

admin.site.register(Course , AdminCourse)