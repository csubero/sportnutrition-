import itertools
from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify

from backend.models import Category


class Post(models.Model):
	title = models.CharField(max_length=250, unique=True)
	summary = models.TextField()
	body = RichTextField()
	thumb = models.ImageField(default=None)
	slug = models.SlugField(unique=True, max_length=150)

	categories = models.ManyToManyField(Category, default=None, blank=True)

	active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	@staticmethod
	def get_by_id(id):

		try:

			post = Post.objects.get(pk=id)

		except Post.DoesNotExist:

			post = None

		return post

	def save(self, *args, **kwargs):

		self.title = self.title.lower()

		if self.id is None:

			max_length = Post._meta.get_field('slug').max_length
			self.slug = slugify(self.title)[:max_length]
			for x in itertools.count(1):
				if not Post.objects.filter(slug=self.slug).exists():
					break
				self.slug = '%s-%d' % (self.slug, x)

		super(Post, self).save(*args, **kwargs)
