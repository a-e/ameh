Development
===========

It's a good idea to run ameh in a virtualenv, especially during development.
The short version::

    $ pip install virtualenvwrapper
    $ mkvirtualenv ameh
    $ pip install -r requirements.txt

Due to the preponderance of really old Python versions in enterprise
environments like CentOS, the code in ameh is designed to be compatible with
Python 2.4. If you contribute new code to ameh, please avoid using features from
newer versions of Python.

Unit tests are in the ``tests`` directory. You can run them with `py.test`_ like
this::

    $ py.test

.. _py.test: http://pytest.org/

