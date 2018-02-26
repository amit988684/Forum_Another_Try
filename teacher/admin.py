from django.contrib import admin
from .models import DocumentTeacher,TeacherModel,Assignment,Slide
# Register your models here.

admin.site.register(DocumentTeacher)
admin.site.register(TeacherModel)
admin.site.register(Assignment)
admin.site.register(Slide)
