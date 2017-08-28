from django.forms import ModelForm, Textarea

from backend.models import Question


class QuestionForm(ModelForm):
	class Meta:
		model = Question

		fields = ['english_question', 'spanish_question']

		widgets = {
			'english_question': Textarea(attrs={'class': 'form-control'}),
			'spanish_question': Textarea(attrs={'class': 'form-control'}),
		}
