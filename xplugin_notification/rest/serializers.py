# coding=utf-8
from django.utils import html
from rest_framework import serializers


class NotificationSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(source="pk")
	message = serializers.SerializerMethodField('get_message')
	url = serializers.SerializerMethodField("get_absolute_url", read_only=True)

	def get_absolute_url(self, instance):
		return instance.url

	def get_message(self, instance):
		# handle xss
		return html.escape(str(instance.message))

	class Meta:
		fields = (
			'id',
			'message',
			'url',
			'is_read',
			'read_datetime'
		)
