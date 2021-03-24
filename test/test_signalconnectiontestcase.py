from django_test_signals import SignalConnectionTestCase

class SignalConnectionTestCaseUnitTest(SignalConnectionTestCase):
	expected_request_started = [
		'django.db.close_old_connections',
		'django.db.reset_queries',
	]
	expected_request_finished = [
		#'django.core.handlers.base.reset_urlconf'
		'django.core.cache.close_caches',
		'django.db.close_old_connections',
	]
	expected_pre_delete = ['django.contrib.sites.models.clear_site_cache']
	expected_pre_save = ['django.contrib.sites.models.clear_site_cache']
	expected_pre_migrate = [
		'django.contrib.contenttypes.management.inject_rename_contenttypes_operations'
	]
	expected_post_migrate = [
		'django.contrib.auth.management.create_permissions',
		'django.contrib.contenttypes.management.create_contenttypes',
		'django.contrib.sites.management.create_default_site',
	]
	expected_setting_changed = [
		#'django.core.files.storage._clear_cached_properties',
		'django.contrib.auth.hashers.reset_hashers',
		'django.test.signals.auth_password_validators_changed',
		'django.test.signals.clear_cache_handlers',
		'django.test.signals.clear_routers_cache',
		'django.test.signals.clear_serializers_cache',
		'django.test.signals.complex_setting_changed',
		'django.test.signals.file_storage_changed',
		'django.test.signals.language_changed',
		'django.test.signals.localize_settings_changed',
		'django.test.signals.reset_template_engines',
		'django.test.signals.root_urlconf_changed',
		'django.test.signals.static_finders_changed',
		'django.test.signals.static_storage_changed',
		'django.test.signals.update_connections_time_zone',
		'django.test.signals.update_installed_apps',
		'django.test.signals.user_model_swapped',
		'django.utils.translation.trans_real.reset_cache',
	]
