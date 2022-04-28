# from https://learndjango.com/tutorials/django-signup-tutorial
import time

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accounts.forms import UserCreateForm
from django.urls import reverse_lazy
from django.views import generic, View
from .forms import UserDeleteForm
from django.shortcuts import render, redirect
from django.contrib import messages


class SignUpView(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


# from https://www.reddit.com/r/webdev/comments/cjfmg8/django_deleting_user_accounts/
@method_decorator(login_required, name='dispatch')
class DeleteUserView(View):
    form_class = UserDeleteForm
    template_name = 'delete_account.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=request.user)
        if form.is_valid():
            user = request.user
            user.delete()
            return redirect('home')
        return render(request, self.template_name, {'form': form})
