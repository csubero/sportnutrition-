from django.shortcuts import render
from django.views import View

from backend.models import Post


class IndexView(View):
	template_name = 'frontend/index/_index.html'

	def get(self, request):
		context = {}
		recent_posts = Post.objects.filter(status=Post.PUBLISH, active=True).order_by('-created_at')

		context['recent_posts'] = recent_posts

		return render(request, self.template_name, context=context)


class IndexTemporalView(View):
	template_name = 'frontend/index/index.html'

	def get(self, request):
		return render(request, self.template_name)
