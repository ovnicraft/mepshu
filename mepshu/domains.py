# -*- coding: utf-8 -*-

"""
mailgun.domains


"""

import requests

from .core import Mailgun
from .decorators import check_type


class Domain(object):

    def __init__(self, data):
        self.created_at = data['created_at']
        self.smtp_login = data['smtp_login']
        self.name = data['name']
        self.smtp_password = data['smtp_password']
        self.wildcard = data['wildcard']
        self.spam_action = data['spam_action']
        self.state = data['state']
        

class Domains(Mailgun):

    items = []

    def __init__(self, session):
        self.session = session
        self.items = []
        self.entity_path = 'domains'

    def __getitem__(self, key):
        return self.items[key]

    def api_url(self):
        """
        URL for domains
        """
        url = super(Domains, self).api_url()
        return url + '/' + self.entity_path

    def parse(self, response):
        data = response.json()
        dms = []
        if data.get('total_count') > 0:
            dms = [Domain(item) for item in data['items']]
        return dms

    @check_type
    def get(self):
        """
        Get domains list
        """
        response = requests.get(self.api_url(), auth=self.session.auth)
        self.items = self.parse(response)
