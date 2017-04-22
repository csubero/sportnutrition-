from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm, TextInput

from backend.models import Tip


class TipForm(ModelForm):


	class Meta:
		model=Tip
		fields=['title', 'content', 'active']

		widgets={
			'title': TextInput(attrs={'class': 'form-control border-input'}),
			'content': CKEditorWidget(),
		}