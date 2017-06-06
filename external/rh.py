import requests
import json

from envparse import env
env.read_envfile("local.env")


class HubGet():
    """
    Remittance Hub API wrapper
    """

    def __init__(self, **kwargs):
        self.authorization = kwargs['authorization']
        self.source_reference_number = kwargs['source_reference_number']
        self.partner_id = kwargs['partner_id']

    def get_remittance(self):
        url = env("RH_URL")
        key = env("RH_KEY")
        crt = env("RH_CRT")
        payload = {
                "partner_id": self.partner_id,
                "source_reference_number": self.source_reference_number}
        headers = {
                "content-type": "application/json",
                "AUTHORIZATION": self.authorization}
        response = requests.post(
                                url,
                                data=json.dumps(payload),
                                headers=headers,
                                cert=(crt, key))
        return response.json()
