from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
import requests
import json

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
        url = "https://3.85.44.32/api/public/request_kasm"
        payload = json.dumps({
            "api_key": "q7I5MJFnoX16",
            "api_key_secret": "hMN3qhkcibkk1wc9US7R1QalcaPZEHiD",
            "user_id": "e60a9c80-289a-4b3a-aedb-42f1d5fe8060",
            "image_id": "51187e08ea6f4aaa982c9a8c0ed947ee",
            "enable_sharing": "true",
            "environment": {
                "ENV_VAR": ""
            }
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload, verify=False)
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
        url = "https://3.85.44.32/api/public/destroy_kasm"
        id = LaunchContext.objects.get().instance_id
        payload = json.dumps({
            "api_key": "q7I5MJFnoX16",
            "api_key_secret": "hMN3qhkcibkk1wc9US7R1QalcaPZEHiD",
            "user_id": "e60a9c80-289a-4b3a-aedb-42f1d5fe8060",
            "kasm_id": id
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload, verify=False)
        print(response.text)

    except:
        print("No active sessions")

    LaunchContext.objects.all().delete()
    return HttpResponseRedirect(reverse('index'))
