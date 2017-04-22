import itertools
from django.db import models
from django.template.defaultfilters import slugify


class Tip(models.Model):
	title = models.CharField(max_length=150)
	content = models.TextField()
	slug = models.SlugField(unique=True, max_length=150)

	active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title.title()

	@staticmethod
	def get_by_id(tip_id):

		try:

			tip = Tip.objects.get(pk=tip_id)

		except Tip.DoesNotExist:

			tip = None

		return tip

	def save(self, *args, **kwargs):

		self.title = self.title.lower()

		if self.id is None:

			max_length = Tip._meta.get_field('slug').max_length
			self.slug = slugify(self.title)[:max_length]
			for x in itertools.count(1):
				if not Tip.objects.filter(slug=self.slug).exists():
					break
				self.slug = '%s-%d' % (self.slug, x)

		super(Tip, self).save(*args, **kwargs)
