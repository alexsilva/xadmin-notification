from django.conf import settings
from django.utils.module_loading import import_string
from xadmin.sites import site
from xadmin.views import ModelAdminView, CommAdminView, ListAdminView
import xadmin.sites

from xplugin_notification.models import Notification
from xplugin_notification.plugin import NotificationAdminPlugin, NotificationMenuPlugin, GuardianAdminPlugin

site.register_plugin(NotificationAdminPlugin, ModelAdminView)
site.register_plugin(NotificationMenuPlugin, CommAdminView)
site.register_plugin(GuardianAdminPlugin, ListAdminView)


NotificationAdminOpts = getattr(settings, "NOTIFICATION_ADMIN_OPTS", object)
if isinstance(NotificationAdminOpts, str):
	NotificationAdminOpts = import_string(NotificationAdminOpts)


@xadmin.sites.register(Notification)
class NotificationAdmin(NotificationAdminOpts):
	# plugin NotificationAdminPlugin
	notification_active = True

	# plugin GuardianAdminPlugin
	notification_guardian_protected = True

	list_filter = (
		"recipient",
		"source",
		"is_read",
	)

	search_fields = (
		"message",
		"url"
	)

	list_display = (
		"recipient",
		"message",
		"source",
		"url",
		"is_read",
		"read_datetime"
	)
