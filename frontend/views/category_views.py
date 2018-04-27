from django.views.generic import DetailView

from backend.models import Category


class CategoryDetailView(DetailView):
	model = Category

	template_name = 'frontend/category/detail.html'
