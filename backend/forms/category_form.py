from django.forms import ModelForm, TextInput

from backend.models import Category


class CategoryForm(ModelForm):
	class Meta:
		model = Category
		fields = ['name']

		widgets = {
			'name': TextInput(attrs={'class': 'form-control border-input'}),
		}
