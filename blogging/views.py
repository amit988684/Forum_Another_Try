from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from teacher.views import teacher_profile

# Create your views here.
#
# def index(request):
#     return render(request,'index.html',{})


def user_login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:

            # check if the user is a superuser
            if user.is_superuser:
                login(request, user)
                return HttpResponse("<h1>super users</h1>")
            # checks if the user is active and is not a staff     ... then he is a STUDENT
            if user.is_active and not user.is_staff:
                login(request, user)
                return HttpResponse('You are logged in as student')

            # checks if user is active and is a staff       ... then he is a TEACHER
            if user.is_active and user.is_staff:
                login(request, user)
                return HttpResponseRedirect(reverse(teacher_profile, args=[request.user.username]))
                # return account_redirect(request)
            return render(request,'registration/login.html', {'user': user})
        else:
            return render(request, 'registration/login.html', {'error': 'wrong username or password !!!'})
    return render(request, 'registration/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))
        # here the reverse ('user_login') ...
        # the 'user_login' is matched to the name in urlpatterns and returns that particuler view