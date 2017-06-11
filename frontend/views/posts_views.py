from django.views.generic import DetailView

from backend.models import Post, Category


class PostDetailView(DetailView):
	model = Post

	template_name = 'frontend/post/post_single.html'

	context_object_name = 'post'

	def get_context_data(self, **kwargs):
		data = super(PostDetailView, self).get_context_data(**kwargs)

		data['categories'] = Category.objects.all().order_by('name')

		return data
