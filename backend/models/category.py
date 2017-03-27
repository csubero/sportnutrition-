import itertools
from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
	name = models.CharField(max_length=150, unique=True)
	slug = models.CharField(unique=True, max_length=150)

	active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def save(self, *args, **kwargs):

		self.name = self.name.lower()

		if self.id is None:

			max_length = Category._meta.get_field('slug').max_length
			self.slug = slugify(self.name)[:max_length]
			for x in itertools.count(1):
				if not Category.objects.filter(slug=self.slug).exists():
					break
				self.slug = '%s-%d' % (self.slug, x)

		super(Category, self).save(*args, **kwargs)
