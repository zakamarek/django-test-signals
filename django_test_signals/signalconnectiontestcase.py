'Django test cases which helps to test Django signals.'

from django.core import signals as core_signals
from django.db.backends import signals as backend_signals
from django.db.models import signals as model_signals
from django.test import SimpleTestCase, signals as test_signals


class SignalConnectionTestCase(SimpleTestCase):
	'Parent class for test cases which verifies if Django signals are connected.'

	# core signals
	expected_got_request_exception = []
	expected_request_started = []
	expected_request_finished = []

	# db backends signals
	expected_connection_created = []

	# db models signals
	expected_class_prepared = []
	expected_m2m_changed = []

	expected_pre_delete = []
	expected_pre_init = []
	expected_pre_migrate = []
	expected_pre_save = []

	expected_post_delete = []
	expected_post_init = []
	expected_post_migrate = []
	expected_post_save = []

	# test signals
	expected_setting_changed = []
	expected_template_rendered = []

	@staticmethod
	def get_full_name(receiver):
		'Returns full canonical name of the signal receiver'
		receiver = receiver[1]()
		if receiver:
			return receiver.__module__ + '.' + receiver.__name__
		return None

	def verify(self, expected, django_receivers):
		'Verifies if all expected signals exist among given Django receivers'
		django_receivers = [self.get_full_name(r) for r in django_receivers if self.get_full_name(r)]
		print(django_receivers)
		for function in expected:
			self.assertIn(function, django_receivers)

	def test_signal_connections(self):
		'Verifies if all declared lists of signals exist among discovered Django receivers'
		# core signals
		self.verify(
			self.expected_got_request_exception, core_signals.got_request_exception.receivers
		)
		self.verify(
			self.expected_request_started, core_signals.request_started.receivers
		)
		self.verify(
			self.expected_request_finished, core_signals.request_finished.receivers
		)

		# db backends signals
		self.verify(
			self.expected_connection_created, backend_signals.connection_created.receivers
		)

		# db models signals
		self.verify(
			self.expected_class_prepared, model_signals.class_prepared.receivers
		)

		self.verify(self.expected_m2m_changed, model_signals.m2m_changed.receivers)

		self.verify(self.expected_pre_delete, model_signals.pre_delete.receivers)
		self.verify(self.expected_pre_init, model_signals.pre_init.receivers)
		self.verify(self.expected_pre_migrate, model_signals.pre_migrate.receivers)
		self.verify(self.expected_pre_save, model_signals.pre_save.receivers)

		self.verify(self.expected_post_delete, model_signals.post_delete.receivers)
		self.verify(self.expected_post_init, model_signals.post_init.receivers)
		self.verify(self.expected_post_migrate, model_signals.post_migrate.receivers)
		self.verify(self.expected_post_save, model_signals.post_save.receivers)

		# test signals
		self.verify(
			self.expected_setting_changed, test_signals.setting_changed.receivers
		)
		self.verify(
			self.expected_template_rendered, test_signals.template_rendered.receivers
		)
