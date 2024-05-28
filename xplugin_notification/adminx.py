from xadmin.sites import site
from xadmin.views import ModelAdminView
import xadmin.sites

from xplugin_notification.models import Notification
from xplugin_notification.plugin import NotificationAdminPlugin

site.register_plugin(NotificationAdminPlugin, ModelAdminView)


@xadmin.sites.register(Notification)
class NotificationAdmin:
	...
