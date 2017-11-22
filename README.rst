===============
pytest-env-info
===============

.. image:: https://travis-ci.org/abadger/pytest-env-info.svg?branch=master
    :target: https://travis-ci.org/abadger/pytest-env-info
    :alt: See Build Status on Travis CI

Push information about the running pytest into the environment


Features
--------

* Injects information about the Python and Pytest versions that are running the unittests into the
  environment.  This can be used for configuring other pytest plugins for the Python version being run
  on.


Requirements
------------

* Pytest


Installation
------------

You can install "pytest-env-info" via `pip`_ from `PyPI`_::

    $ pip install pytest-env-info


Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-env-info" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`BSD-3`: http://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: http://www.gnu.org/licenses/gpl-3.0.txt
.. _`Apache Software License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/abadger/pytest-env-info/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.python.org/pypi/pip/
.. _`PyPI`: https://pypi.python.org/pypi
