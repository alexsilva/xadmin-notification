from django.contrib.auth import get_permission_codename
from guardian.shortcuts import assign_perm

from xplugin_notification.models import Notification

__all__ = ["notification", "NotificationAdmin"]


class NotificationAdmin:
	"""Object that registers the notifications that will be delivered to the user"""

	notification_model = Notification
	permission_names = ("view", "add", "change", "delete")

	def __init__(self):
		self.opts = self.notification_model._meta

	def notify(self, recipient, message: str, source=None, slug=None, **options) -> Notification:
		"""Notifies a users"""
		if not (recipient.is_staff and recipient.is_active):
			# only sends notifications to active staff and users.
			return
		defaults = dict(options)
		defaults.update(message=message)
		obj, created = self.notification_model.objects.update_or_create(
			slug=slug,
			recipient=recipient,
			source=source,
			defaults=defaults
		)
		# register permission for object.
		for perm_name in self.permission_names:
			permission_codename = get_permission_codename(perm_name, self.opts)
			assign_perm(permission_codename, recipient, obj)
		return obj

	def notify_groups(self, groups: tuple, message: str, source=None, **options):
		"""Notifies a list of user groups"""
		notifications = []
		for group in groups:
			for user in group.user_set.filter(is_staff=True, is_active=True):
				notifications.append(
					self.notify(user, message, source=source, **options)
				)
		return notifications


notification = NotificationAdmin()
