from django.shortcuts import render
from .models import TeacherModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,DeleteView,TemplateView,UpdateView
# Create your views here.


# test function
@login_required
def teacher_profile(request, username):
    user = User.objects.get(username=username)
    teacher = TeacherModel.objects.get(user=user)
    context = {'teacher': teacher, 'user': user}
    return render(request, 'teacher_profile.html', context=context)

# class TeacherCourseView(LoginRequiredMixin,ListView):
#     model = TeacherModel
#     template_name = "teacher_profile.html"
#     context_object_name = "course"