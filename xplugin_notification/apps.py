from django.apps import AppConfig


class XpluginNotificationConfig(AppConfig):
	name = 'xplugin_notification'
	verbose_name = 'Notificação do admin'

	def ready(self):
		...
