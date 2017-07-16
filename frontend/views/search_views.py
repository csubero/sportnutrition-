from django.shortcuts import render
from django.views import View


class SearchView(View):
	template_name = 'frontend/search/search_template.html'

	def get(self, request):
		return render(request, self.template_name)
