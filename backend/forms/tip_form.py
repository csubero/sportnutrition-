from django.forms import ModelForm, TextInput, Textarea, Select

from backend.models import Tip


class TipForm(ModelForm):
	class Meta:
		model = Tip

		fields = ['title', 'content', 'tip_type', 'active']

		widgets = {
			'title': TextInput(attrs={'class': 'form-control border-input'}),
			'content': Textarea(),
			'tip_type': Select(attrs={'class': 'form-control border-input'}),
		}
