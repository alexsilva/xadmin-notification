from django.conf import settings
from django.utils.module_loading import import_string
from xadmin.sites import site
from xadmin.views import ModelAdminView, CommAdminView, ListAdminView
import xadmin.sites

from xplugin_notification.actions import MarkAsReadAction
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
	actions = (MarkAsReadAction,)

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
		"url_display",
		"is_read",
		"read_datetime"
	)

	def url_display(self, instance):
		"""Url display field"""
		return f"<a href='{instance.url}'>{instance.url}</a>" if instance.url else ""

	url_display.short_description = "URL"
	url_display.admin_order_field = "url"
	url_display.is_column = True
	url_display.allow_tags = True
