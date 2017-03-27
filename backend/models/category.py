from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=150, unique=True)
	slug = models.CharField(unique=True, max_length=150)

	active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
