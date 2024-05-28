from rest_framework.exceptions import PermissionDenied
from xadmin.views import BaseAdminPlugin

from xplugin_notification.rest.permisstion import HasNotificationPermission
from xplugin_notification.rest.serializers import NotificationSerializer


class NotificationAdminPlugin(BaseAdminPlugin):
	"""Plugin that filters the content and returns it in rest style"""
	notification_serializer_class = NotificationSerializer
	notification_permissions = [HasNotificationPermission]
	notification_request_param = "xnotification"
	notification_active = True

	def init_request(self, *args, **kwargs):
		is_active = bool(self.notification_active and self.request.GET.get('plugin') == self.notification_request_param)
		# The plugin is read-only because the permissions have been rewritten.
		if is_active and self.admin_view.request_method not in ['get', 'options', 'head']:
			raise PermissionDenied('read only')
		return is_active

	def get_permissions(self, __):
		"""Validates only list permissions"""
		return [permission() for permission in self.notification_permissions]

	def get_serializer_class(self, __):
		serializer_class = self.notification_serializer_class
		meta = serializer_class.Meta
		serializer_class = type(serializer_class.__name__, (serializer_class,), {
			'Meta': type("Meta", (meta,), {'model': self.model})
		})
		return serializer_class

	def filter_queryset(self, queryset, *args, **kwargs):
		return queryset
