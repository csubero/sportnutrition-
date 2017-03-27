from django.db import models


class Post(models.Model):
	title = models.CharField(max_length=250, unique=True)
	summary = models.TextField()
	body = models.TextField()
	thumb = models.ImageField(default=None)
	slug = models.SlugField(unique=True, max_length=150)

	active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
