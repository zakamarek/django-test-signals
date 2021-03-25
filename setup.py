'Django test case which helps to test Django signals.'

from setuptools import setup

setup(
	name = 'django-test-signals',
	version = '0.0.5',
	packages = ['django_test_signals'],
	install_requires = ['django>=1.0'],
	author = 'Zakamarek',
	author_email = 'Zakamarek.REMOVETHIS@gmail.AND.THIS.com',
	description = __doc__,
	long_description = __doc__,
	url = 'https://github.com/zakamarek/django-test-signals',
	license='MIT',
	platforms='ALL',
	classifiers = [
		'Intended Audience :: Developers',
		'Programming Language :: Python',
		'Topic :: Software Development :: Libraries :: Python Modules',
	],
)
