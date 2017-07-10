import itertools
from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify

from django.utils.translation import ugettext as _

from backend.models import Category


class Post(models.Model):
	# post Status options
	DRAFT = 1
	PUBLISH = 2
	UNPUBLISH = 3

	POST_STATUS = (
		(DRAFT, _('Draft')),
		(PUBLISH, _('Published')),
		(UNPUBLISH, _('Unpublished'))
	)

	POST = 1
	TIP = 2
	DIET = 3

	POST_TYPE = (
		(POST, 'Post'),
		(TIP, 'Tip'),
		(DIET, 'Diet')
	)

	title = models.CharField(max_length=250, unique=True)
	summary = models.TextField()
	body = models.TextField()
	thumb = models.ImageField(default=None, upload_to='thumbs/%Y/%m/%d')
	slug = models.SlugField(unique=True, max_length=150)
	status = models.IntegerField(default=DRAFT, choices=POST_STATUS)
	type = models.IntegerField(default=POST, choices=POST_TYPE)

	categories = models.ManyToManyField(Category, default=None, blank=True)

	active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):

		return self.title.title()

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

	def delete(self, *args, **kwargs):

		if self.thumb is not None:
			self.thumb.delete()

		super(Post, self).delete(*args, **kwargs)
