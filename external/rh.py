import requests
import json

from envparse import env


class HubGet():
    """
    Remittance Hub API wrapper
    """

    def __init__(self, **kwargs):
        self.authorization = kwargs['authorization']
        self.source_reference_number = kwargs['source_reference_number']
        self.partner_id = kwargs['partner_id']
        self.url = kwargs.get("RH_URL", None)
        self.key = kwargs.get("RH_KEY", None)
        self.crt = kwargs.get("RH_CRT", None)

    def get_remittance(self):
        payload = {
                "partner_id": self.partner_id,
                "source_reference_number": self.source_reference_number}
        headers = {
                "content-type": "application/json",
                "AUTHORIZATION": self.authorization}
        response = {"url":url,"key":key,"crt":crt}
        return response
        response = requests.post(
                                url,
                                data=json.dumps(payload),
                                headers=headers,
                                cert=(crt, key))
        return response.json()
