from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

from DigitalLogic.views import SignUpView, DeleteUserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("delete_account/", DeleteUserView.as_view(), name='delete_account'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('launcher', include("Launcher.urls"), name='index'),
]
