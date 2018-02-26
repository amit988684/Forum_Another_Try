from django.contrib import admin
from .models import StudentModel,Course,Depart,DocumentStudent
# Register your models here.

admin.site.register(StudentModel)
admin.site.register(Course)
admin.site.register(Depart)
admin.site.register(DocumentStudent)
