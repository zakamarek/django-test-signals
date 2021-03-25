# django-test-signals

Testing, if Django signals are connected, may be tricky, because mocking or importing the file with the receiver results in connecting it.
`SignalConnectionTestCase` solves this problem using introspection to check if the declared receivers are connected.
To use this test just inherit `SignalConnectionTestCase` and put full / canonical names into appropriate fields.
For example if you want to test some built-in Django site signals you can do as follows:

```python
class DjangoSiteBuiltinSignalConnectionTestCase(SignalConnectionTestCase):
	expected_pre_save = ['django.contrib.sites.models.clear_site_cache']
```


## Installation ##
`pip install django-test-signals`


## Requirements ##
* Python 2 or 3
* Django


## Tests ##
If you're interested in the project and you contribute, please make sure:
* your changes don't break current tests
* you add appropriate tests for your features/bug fixes.

To run the tests simply use
`./runtests.py`

