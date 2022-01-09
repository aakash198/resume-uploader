from django.contrib import admin
from django.db import models
from .models import resume
# Register your models here.

@admin.register(resume)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display=['id','name','dob','gender','locality','city','pin','state','mobile','email','job_city','profile_image','my_file']
