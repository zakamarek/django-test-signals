# django-test-signals

Testing if Django signals are connected may be tricky, because mocking or importinting the file with the receiver results in connecting it.
`SignalConnectionTestCase` solves this problem using introspection to check if the declared receivers are connected.
To use this test just inherit `SignalConnectionTestCase` and put full / canonical names into appropriate fields.
For example if you want to test some built-in Django site signals you can do as follows:

```python
class DjangoSiteBuiltinSignalConnectionTestCase(SignalConnectionTestCase):
	expected_pre_save = ['django.contrib.sites.models.clear_site_cache']
```

