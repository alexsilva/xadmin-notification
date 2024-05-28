from xplugin_notification.models import Notification

__all__ = ["notification"]


class NotificationRegister:
	"""Object that registers the notifications that will be delivered to the user"""

	notification_model = Notification

	def __init__(self):
		...

	def notify(self, recipient, message: str, source=None, **options):
		"""Notifies a users"""
		return self.notification_model.objects.create(
			recipient=recipient,
			source=source,
			message=message,
			**options
		)

	def notify_groups(self, groups: tuple, message: str, source=None, **options):
		"""Notifies a list of user groups"""
		notifications = []
		for group in groups:
			for user in group.user_set.all():
				notifications.append(
					self.notify(user, message, source=source, **options)
				)
		return notifications


notification = NotificationRegister()
