from django.contrib import admin
from myapp.models import Student
class StudentAdmin(admin.ModelAdmin):
	list_display=['no','name','mobile','city','course']
admin.site.register(Student,StudentAdmin)
# Register your models here.
