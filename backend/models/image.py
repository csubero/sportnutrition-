from django.db import models

from backend.models.gallery import Gallery


class Image(models.Model):
	title = models.CharField(max_length=150, null=True, blank=True)
	image = models.ImageField()
	order = models.IntegerField(default=0)

	gallery = models.ForeignKey(Gallery, default=None, null=True, related_name='images')

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title.title()
