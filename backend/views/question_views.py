from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from backend.forms.question_form import QuestionForm
from backend.models import Question


class QuestionListView(ListView):
	model = Question

	template_name = 'backend/question/question_index.html'

	context_object_name = 'question_list'


class QuestionCreateView(CreateView):
	model = Question

	template_name = 'backend/question/question_form.html'

	form_class = QuestionForm

	def get_context_data(self, **kwargs):
		data = super(QuestionCreateView, self).get_context_data(**kwargs)

		data['title_form'] = 'Add Question'

		data['reverse_url'] = reverse_lazy('backend.question.index')

		return data
