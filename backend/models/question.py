import uuid

from django.db import models


class Question(models.Model):
	english_question = models.TextField()
	spanish_question = models.TextField()
	external_id = models.UUIDField(default=uuid.uuid4, unique=True)

	active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
