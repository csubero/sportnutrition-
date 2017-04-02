from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from backend.forms import CategoryForm
from backend.models import Category


class CategoryIndexView(View):
	template_name = 'backend/category/category_form.html'

	def get(self, request):
		form = CategoryForm

		category_list = Category.objects.all().order_by('name')

		return render(request, self.template_name, {'form': form, 'category_list': category_list})

	def post(self, request):
		form = CategoryForm(request.POST)

		if form.is_valid():
			form.save()

			return redirect(reverse('backend.category.index'))

		category_list = Category.objects.all().order_by('name')

		return render(request, self.template_name, {'form': form, 'category_list': category_list})


class CategoryDeleteView(View):
	def post(self, request):
		category_id = request.POST.get("category_id")

		category = Category.get_by_id(category_id)

		if category is not None:
			category.delete()

		return redirect(reverse('backend.category.index'))
