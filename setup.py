from setuptools import setup

setup(
	name='xadmin-notification',
	version='1.1.0',
	packages=[
		'xplugin_notification',
		'xplugin_notification.rest',
		'xplugin_notification.migrations'
	],
	include_package_data=True,
	url='https://github.com/alexsilva/xadmin-content-url',
	license='MIT',
	author='Alex',
	author_email='',
	description='Notification system for administration users.'
)
