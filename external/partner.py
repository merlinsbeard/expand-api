import requests
import json


class Partner(object):
    """
    Wrapper for branch
    """

    def __init__(self, **kwargs):
        self.token = kwargs.get('token', None)
        self.partner_id = kwargs.get('partner_id', None)
        self.partner_url = kwargs.get('partner_url')
        self.branch_url = kwargs.get('branch_url')

    def get_partners(self):
        url = f'{self.partner_url}/private/0/partners'
        r = requests.get(url)
        return r.json()

    def get_partners_one(self):
        url = f'{self.partner_url}/private/0/partners/{self.partner_id}'
        r = requests.get(url)
        return r.json()

    def get_branches(self):
        url = f'{self.branch_url}/api/0/branches'
        headers = {"AUTHORIZATION": self.token}
        r = requests.get(url, headers=headers)
        return r.json()

    def get_branches_one(self, branch_code):
        data = self.get_branches()
        for d in data:
            if d['branch_code'] == branch_code:
                return d
        else:
            return {"status": "FAIL"}
