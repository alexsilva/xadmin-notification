from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class XpluginNotificationConfig(AppConfig):
	name = 'xplugin_notification'
	verbose_name = _('Notifications (admin)')

	def ready(self):
		...
