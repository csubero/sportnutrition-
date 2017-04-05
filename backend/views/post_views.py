from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView

from backend.forms.post_form import PostForm
from backend.models import Post


class PostListView(ListView):
	model = Post

	template_name = 'backend/post/post_index.html'

	context_object_name = 'post_list'


class PostCreateView(CreateView):
	model = Post

	template_name = 'backend/post/post_form.html'

	form_class = PostForm

	def get_success_url(self):
		return reverse_lazy('backend.post.edit', kwargs={'pk': self.object.id})

	def get_context_data(self, **kwargs):
		data = super(PostCreateView, self).get_context_data(**kwargs)

		data['title_form'] = 'Add new Post'

		return data


class PostUpdateView(UpdateView):
	model = Post

	template_name = 'backend/post/post_form.html'

	form_class = PostForm

	def get_success_url(self):
		return reverse('backend.post.index')

	def get_context_data(self, **kwargs):
		data = super(PostUpdateView, self).get_context_data(**kwargs)

		data['title_form'] = self.object.title.title()

		return data


class PostDeleteView(View):
	def post(self, request):
		post_id = request.POST.get('post_id')

		post_delete = Post.get_by_id(post_id)

		if post_delete is not None:
			post_delete.delete()

		return redirect(reverse('backend.post.index'))
