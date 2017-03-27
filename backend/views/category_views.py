from django.shortcuts import render
from django.views import View

from backend.forms import CategoryForm
from backend.models import Category


class CategoryIndexView(View):
	template_name = 'backend/category/category_form.html'

	def get(self, request):
		form = CategoryForm

		category_list = Category.objects.all().order_by('name')

		return render(request, self.template_name, {'form': form, 'category_list': category_list})
