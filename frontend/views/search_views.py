from django.shortcuts import render
from django.views import View

from backend.models import Post


class SearchView(View):
	template_name = 'frontend/search/search_template.html'

	def get(self, request):
		search_str = request.GET.get('search_str', None)

		context = {}

		if search_str:
			filters = {
				'active': True,
				'status': Post.PUBLISH,
				'title__contains': search_str.lower(),
			}

			search_results = Post.objects.filter(**filters)

			context = {
				'search_str': search_str,
				'search_results': search_results,
			}

		return render(request, self.template_name, context=context)
