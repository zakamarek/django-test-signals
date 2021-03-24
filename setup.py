'Django test case which helps to test Django signals.'

from setuptools import setup

setup(
	name = 'django-test-signals',
	version = '0.0.1',
	py_modules = ['django_test_signals'],
	install_requires = ['django>=1.0'],
	author = 'Zakamarek',
	author_email = 'Zakamarek@gmail.com',
	description = __doc__,
	url = 'https://github.com/zakamarek/django-test-signals',
	license='MIT',
	platforms='ALL',
	classifiers = [
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT',
		'Programming Language :: Python',
		'Topic :: Software Development :: Libraries :: Python Modules',
	],
)
