import json

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from Launcher.clients import LauncherClient
from Launcher.models import *


def index(request):
    launches = LaunchContext.objects.filter()
    errors = ErrorContext.objects.filter()
    context = {
        'launches': launches,
        'errors': errors,
    }
    return render(request, 'Launcher/index.html', context=context)


def add(request):
    try:
        client = LauncherClient()
        response = client.request_container()

        print(response.text)
        launch_url = json.loads(response.text)['kasm_url']
        instance_id = json.loads(response.text)['kasm_id']
        launch = LaunchContext(launch_url=launch_url, instance_id=instance_id)
        launch.save()

    except:
        print("Session already active")

    return HttpResponseRedirect(reverse('index'))


def destroy(request):
    try:
        container_id = LaunchContext.objects.get().instance_id
        client = LauncherClient()
        response = client.destroy_container(container_id)
        print(response.text)

    except:
        print("No active sessions")

    LaunchContext.objects.all().delete()
    return HttpResponseRedirect(reverse('index'))