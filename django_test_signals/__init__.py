'Django test case which helps to test Django signals.'

import django.utils.version

from .signalconnectiontestcase import SignalConnectionTestCase


__all__ = ['VERSION', '__version__', 'SignalConnectionTestCase']

VERSION = (0, 0, 4, 'alpha', 0)

__version__ = django.utils.version.get_version(VERSION)
