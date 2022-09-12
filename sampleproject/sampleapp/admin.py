from django.contrib import admin

from sampleapp.models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','roll','name','city']