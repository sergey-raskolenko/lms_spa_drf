import re
from rest_framework import serializers

ALLOWED_URLS = ["https://www.youtube.com/"]


class LessonUrlValidator:

	def __init__(self, field):
		self.field = field

	def __call__(self, value):
		for url in ALLOWED_URLS:
			value = dict(value).get(self.field)
			if value:
				if not re.search(url, value):
					raise serializers.ValidationError(f"Указанная ссылка {value} не разрешена")


class CourseUrlValidator:

	def __init__(self, field):
		self.field = field

	def __call__(self, value):
		for url in ALLOWED_URLS:
			value = dict(value).get(self.field)
			if 'https://' in value or 'http://' in value:
				if not re.search(url, value):
					raise serializers.ValidationError(f"Указанная ссылка {value} не разрешена")
