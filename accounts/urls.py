# from https://learndjango.com/tutorials/django-signup-tutorial

from django.urls import path

from .views import SignUpView, DeleteUserView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("delete_account/", DeleteUserView.as_view(), name='delete_account')
]