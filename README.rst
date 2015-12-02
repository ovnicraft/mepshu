===============================
Mailgun Requests
===============================

.. image:: https://img.shields.io/travis/ovnicraft/mailgun-requests.svg
        :target: https://travis-ci.org/ovnicraft/mailgun-requests

.. image:: https://img.shields.io/pypi/v/mailgun-requests.svg
        :target: https://pypi.python.org/pypi/mailgun-requests


Mailgun rfor  Humans

* Free software: BSD license
* Documentation: https://mailgun-requests.readthedocs.org.

Features
--------

* For lists

.. code-block:: python
>>> from mailgun import Session
>>> mg = Session('my_apikey')
>>> mg.lists.add('mylist', 'My new lists')
200
  ...

* For domains

.. code-block:: python
>>> from mailgun import Session
>>> mg = Session('my_apikey')
>>> mg.domains.get()
200
>>> mg.domains[0].name
'example.com'

* TODO
