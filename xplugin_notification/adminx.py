from xadmin.sites import site
from xadmin.views import ModelAdminView, CommAdminView
import xadmin.sites

from xplugin_notification.models import Notification
from xplugin_notification.plugin import NotificationAdminPlugin, NotificationMenuPlugin

site.register_plugin(NotificationAdminPlugin, ModelAdminView)
site.register_plugin(NotificationMenuPlugin, CommAdminView)


@xadmin.sites.register(Notification)
class NotificationAdmin:
	# plugin NotificationAdminPlugin
	notification_active = True

	list_display = (
		"user",
		"message",
		"url",
		"is_read",
		"read_datetime"
	)
