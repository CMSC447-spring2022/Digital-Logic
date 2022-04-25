from django.http import *
from django.shortcuts import HttpResponseRedirect, redirect, render
from django.template import RequestContext
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from LoginPage.models import *

# def index(request):
#     logins = LoginContext.objects.filter()
#     errors = ErrorContext.objects.filter()
#     context = {
#         'logins': logins,
#         'errors': errors,
#     }
#     return render(request, 'login_page/login.html', context=context)


def login_user(request):
    #logout(request)
    #signup(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/main/')
    return HttpResponseRedirect(reverse('login_user'))


@login_required(login_url='/login/')

def login(request, user):
    return


def signup(request):
    ##make signup page view
    return

def logout(request):
    return