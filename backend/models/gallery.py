import itertools
from django.db import models
from django.template.defaultfilters import slugify


class Gallery(models.Model):
	title = models.CharField(max_length=150)

	slug = models.SlugField(unique=True, max_length=150)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title.title()

	def save(self, *args, **kwargs):

		self.title = self.title.lower()

		if self.id is None:

			max_length = Gallery._meta.get_field('slug').max_length
			self.slug = slugify(self.title)[:max_length]
			for x in itertools.count(1):
				if not Gallery.objects.filter(slug=self.slug).exists():
					break
				self.slug = '%s-%d' % (self.slug, x)

		super(Gallery, self).save(*args, **kwargs)
