from django.contrib.admin.widgets import AdminFileWidget
from django.forms import ModelForm, TextInput, Textarea, CheckboxSelectMultiple
from ckeditor.widgets import CKEditorWidget

from backend.models import Post
from backend.utils.widgets import AdminImageWidget


class PostForm(ModelForm):
	class Meta:
		model = Post

		fields = ['title', 'summary', 'body', 'thumb', 'categories']

		widgets = {
			'title': TextInput(attrs={'class': 'form-control border-input'}),
			'summary': Textarea(attrs={'class': 'form-control border-input', 'cols': 1}),
			'body': CKEditorWidget(),
			'thumb': AdminImageWidget(attrs={'class': 'form-control border-input'}),
			'categories': CheckboxSelectMultiple(),
		}
