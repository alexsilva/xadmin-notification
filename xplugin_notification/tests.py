from django.contrib.auth import get_user_model
from django.test import TestCase

from xplugin_notification.register import notification

User = get_user_model()


class NotificationTestCase(TestCase):
	def setUp(self):
		self.slug = 'notifs'
		self.user = User._default_manager.create(
			username='user',
			is_staff=True,
			is_active=True
		)

	def test_update_notification(self):
		"""Tests whether it is possible to update an already sent notification"""
		notifs = notification.notify(self.user, message='Hello World!', slug=self.slug)
		notifs2 = notification.notify(self.user, message='Hello Universe!', slug=self.slug)

		self.assertEquals(notifs, notifs2)
		self.assertNotEquals(notifs.message, notifs2.message)

	def test_creating_notification(self):
		"""Testing notification creation without updating"""
		obj = notification.notify(self.user, message='Hello1')
		obj2 = notification.notify(self.user, message='Hello2')

		self.assertNotEquals(obj, obj2)
