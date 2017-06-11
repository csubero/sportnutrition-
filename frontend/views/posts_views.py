from django.views.generic import DetailView

from backend.models import Post


class PostDetailView(DetailView):

	model = Post

	template_name = 'frontend/post/post_single.html'

	context_object_name = 'post'