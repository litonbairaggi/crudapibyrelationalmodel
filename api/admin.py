from django.contrib import admin

# Register your models here.
from . models import Result
from . models import Student

admin.site.register(Result)
admin.site.register(Student)
