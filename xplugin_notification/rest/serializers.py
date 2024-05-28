# coding=utf-8
from django.utils import html
from django.utils.formats import date_format
from rest_framework import serializers


class NotificationSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(source="pk")
	user_name = serializers.SerializerMethodField("get_user_name")
	user_url = serializers.SerializerMethodField("get_user_url")
	message = serializers.SerializerMethodField('get_message')
	url = serializers.SerializerMethodField("get_absolute_url", read_only=True)
	created = serializers.SerializerMethodField("get_created", read_only=True)

	def get_user_name(self, instance):
		return str(instance.source) if instance.source else ''

	def get_user_url(self, instance):
		return str(instance.source.get_absolute_url()) if instance.source else ''

	def get_absolute_url(self, instance):
		return instance.url

	def get_message(self, instance):
		# handle xss
		return html.escape(str(instance.message))

	def get_created(self, instance):
		return date_format(instance.created_at, format="DATETIME_FORMAT")

	class Meta:
		fields = (
			'id',
			'user_name',
			'user_url',
			'message',
			'url',
			'is_read',
			'read_datetime',
			'created'
		)
