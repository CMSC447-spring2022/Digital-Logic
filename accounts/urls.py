# from https://learndjango.com/tutorials/django-signup-tutorial

from django.urls import path

from .views import SignUpView, deleteuser

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("delete_account/", deleteuser.as_view(), name='delete')
]