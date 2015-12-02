==========================
Mailgun Para Seres Humanos
==========================

.. image:: https://img.shields.io/travis/ovnicraft/mepshu.svg
        :target: https://travis-ci.org/ovnicraft/mepshu

.. image:: https://img.shields.io/pypi/v/mepshu.svg
        :target: https://pypi.python.org/pypi/mepshu


Mailgun Para Seres Humanos

* Free software: BSD license
* Documentation: https://mepshu.readthedocs.org.

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
