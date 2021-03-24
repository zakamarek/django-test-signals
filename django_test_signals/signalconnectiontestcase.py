'Django test cases which helps to test Django signals.'

from django.db.models import signals
from django.test import TestCase


class SignalConnectionTestCase(TestCase):
	'Parent class for test cases which verifies if Django signals are connected.'

	expected_m2m_changed = []
	expected_pre_delete = []
	expected_pre_save = []
	expected_post_delete = []
	expected_post_save = []

	@staticmethod
	def get_full_name(receiver):
		'Returns full canonical name of the signal receiver'
		receiver = receiver[1]()
		return receiver.__module__ + '.' + receiver.__name__

	def verify(self, expected, django_receivers):
		'Verifies if all expected signals exist among given Django receivers'
		receivers = [self.get_full_name(r) for r in django_receivers]
		for function in expected:
			self.assertIn(function, receivers)

	def test_signal_connections(self):
		'Verifies if all declared lists of signals exist among discovered Django receivers'
		self.verify(self.expected_m2m_changed, signals.m2m_changed.receivers)
		self.verify(self.expected_pre_save, signals.pre_save.receivers)
		self.verify(self.expected_post_delete, signals.post_delete.receivers)
		self.verify(self.expected_post_save, signals.post_save.receivers)
