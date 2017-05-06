from django.db import models

from backend.models.gallery import Gallery


class Image(models.Model):
	title = models.CharField(max_length=150, null=True, blank=True)
	file = models.ImageField(upload_to='images/%Y/%m/%d')
	order = models.IntegerField(default=0)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title.title()
