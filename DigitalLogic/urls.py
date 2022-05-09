from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='Launcher/index.html'), name='home'),
    path('launcher', include("Launcher.urls"), name='index'),
]

# urlpatterns += staticfiles_urlpatterns()