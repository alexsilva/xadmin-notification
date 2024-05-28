from xadmin.sites import site
from xadmin.views import ModelAdminView

from xplugin_notification.plugin import NotificationAdminPlugin

site.register_plugin(NotificationAdminPlugin, ModelAdminView)
