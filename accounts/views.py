# from https://learndjango.com/tutorials/django-signup-tutorial

from accounts.forms import UserCreateForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import UserDeleteForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages



class SignUpView(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


# from https://www.reddit.com/r/webdev/comments/cjfmg8/django_deleting_user_accounts/
@login_required
def deleteuser(request):
    if request.method == 'POST':
        delete_form = UserDeleteForm(request.POST, instance=request.user)
        user = request.user
        user.delete()
        messages.info(request, 'Your account has been deleted.')
        return redirect('home')
    else:
        delete_form = UserDeleteForm(instance=request.user)

    context = {
        'delete_form': delete_form
    }

    return render(request, 'accounts/delete_account.html', context)