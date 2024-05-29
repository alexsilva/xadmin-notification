from django.contrib.auth import get_permission_codename
from guardian.shortcuts import assign_perm

from xplugin_notification.models import Notification

__all__ = ["notification"]


class NotificationRegister:
	"""Object that registers the notifications that will be delivered to the user"""

	notification_model = Notification
	permission_names = ("view", "add", "change", "delete")

	def __init__(self):
		self.opts = self.notification_model._meta

	def notify(self, recipient, message: str, source=None, **options):
		"""Notifies a users"""
		obj = self.notification_model.objects.create(
			recipient=recipient,
			source=source,
			message=message,
			**options
		)
		# register permission for object.
		for perm_name in self.permission_names:
			permission_codename = get_permission_codename(perm_name, self.opts)
			assign_perm(permission_codename, recipient, obj)
		return notification

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
