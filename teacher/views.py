from django.shortcuts import render

# Create your views here.


# test function
def teacher_profile(request):
    return render(request, 'teacher_base.html', {})