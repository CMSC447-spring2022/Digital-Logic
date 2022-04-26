import json
import requests


class LauncherClient:
    @staticmethod
    def request_container():
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

        return response

    @staticmethod
    def destroy_container(container_id):
        url = "https://3.85.44.32/api/public/destroy_kasm"

        payload = json.dumps({
            "api_key": "q7I5MJFnoX16",
            "api_key_secret": "hMN3qhkcibkk1wc9US7R1QalcaPZEHiD",
            "user_id": "e60a9c80-289a-4b3a-aedb-42f1d5fe8060",
            "kasm_id": container_id
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload, verify=False)

        return response


    @staticmethod
    def get_all_containers():
        url = "https://3.85.44.32/api/public/get_kasms"

        payload = json.dumps({
            "api_key": "q7I5MJFnoX16",
            "api_key_secret": "hMN3qhkcibkk1wc9US7R1QalcaPZEHiD"
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload, verify=False)

        return response