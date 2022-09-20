from django.contrib import admin
from .models import Student
# Register your models here.
# admin id = admin pass = jsk@886655

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']