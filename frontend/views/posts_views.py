from django.views.generic import DetailView, ListView

from backend.models import Post, Category


class PostIndexView(ListView):
	model = Post

	template_name = 'frontend/post/post_index.html'

	context_object_name = 'posts_list'

	paginate_by = 10

	ordering = 'title'


class PostDetailView(DetailView):
	model = Post

	template_name = 'frontend/post/post_single.html'

	context_object_name = 'post'

	def get_context_data(self, **kwargs):
		data = super(PostDetailView, self).get_context_data(**kwargs)

		data['categories'] = Category.objects.all().order_by('name')

		data['recent_posts'] = Post.objects\
			.filter(active=True, status=Post.PUBLISH)\
			.exclude(id=self.object.id)\
			.order_by('-updated_at')

		return data
