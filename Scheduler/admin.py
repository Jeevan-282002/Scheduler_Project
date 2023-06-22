from django.contrib import admin
from .models import Instructor, Courses, Lectures

# Register your models here.


admin.site.register(Instructor)
admin.site.register(Courses)
admin.site.register(Lectures)