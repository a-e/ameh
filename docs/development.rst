Development
===========

It's a good idea to run ameh in a virtualenv, especially during development.
The short version::

    $ pip install virtualenvwrapper
    $ mkvirtualenv ameh
    $ pip install -r requirements.txt


Testing
-------

ameh is tested with `py.test`_. Install it using pip::

    $ pip install -U pytest

Then run it from the ``ameh`` root directory::

    $ py.test

.. _py.test: http://pytest.org/

