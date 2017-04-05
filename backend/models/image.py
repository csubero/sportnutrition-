from django.db import models


class Image(models.Model):
	title = models.CharField(max_length=150, null=True, blank=True)
	image = models.ImageField()
	order = models.IntegerField(default=0)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
