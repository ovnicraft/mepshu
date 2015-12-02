# -*- coding: utf-8 -*-

"""
"""

import requests

from .core import Mailgun
from .decorators import check_type


class MList(object):
    """
    Mailing list instance
    """
    def __init__(self, data):
        self.name = data['name']
        self.members_count = data['members_count']
        self.description = data['description']
        self.created_at = data['created_at']
        self.access_level = data['access_level']
        self.address = data['address']


class ListsMixin(Mailgun):

    def api_url(self):
        """
        URL for lists
        """
        url = super(ListsMixin, self).api_url()
        return url + '/' + self.entity_path

    def add(self, name_list, description=''):
        """
        Here require API_KEY
        TODO:
        * add exception
        * add decorator to validate session type
        * add check domain
        """
        if not self.session.type == 'private':
            raise "Error"
        data = {
            'address': name_list,
            'description': description
            }
        url = self.api_url()
        response = requests.post(url, auth=self.session.auth, data=data)
        print response.status_code


class Lists(ListsMixin):

    def __init__(self, session):
        self.session = session
        self.items = []
        self.entity_path = 'lists'

    def __getitem__(self, key):
        return self.items[key]

    def __unicode__(self):
        res = ' '.join([u'{0}<{1}>'.format(i.name,i.address) for i in self.items])
        return res

    def __repr__(self):
        return u'{0}'.format(self.__unicode__())

    def parse(self, response):
        data = response.json()
        dms = []
        if data.get('total_count') > 0:
            dms = [MList(item) for item in data['items']]
        return dms

    @check_type
    def get(self):
        """
        Get mailing lists
        """
        response = requests.get(self.api_url(), auth=self.session.auth)
        self.items = self.parse(response)
        print '{0}'.format(response.status_code)
        
