# -*- coding: utf-8 -*-

"""
mailgun.lists


"""
import requests

from .lists import Lists
from .domains import Domains


class Session(requests.Session):
    """
    """
    
    def __init__(self, mg_key):
        session_type, tmp_key = mg_key.split('-')
        self.auth = ('api', mg_key)
        self.type = session_type=='pubkey' and 'public' or 'private'
        self.lists = Lists(self)
        self.domains = Domains(self)
        
