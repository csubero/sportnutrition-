from django.views.generic import ListView

from backend.models import Question


class QuestionListView(ListView):
	model = Question

	template_name = 'backend/question/question_index.html'

	context_object_name = 'question_list'
