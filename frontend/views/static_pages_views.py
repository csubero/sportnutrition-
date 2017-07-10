from django.shortcuts import render
from django.views import View


class AboutPageView(View):
	template_name = 'frontend/static_pages/about_template.html'

	def get(self, request):
		return render(request, self.template_name)
