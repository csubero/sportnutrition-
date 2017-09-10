from django.shortcuts import render
from django.views import View


class QuestionnaireView(View):
	template_name = 'frontend/questionnaire/questionnaire_index.html'

	def get(self, request):
		return render(request, self.template_name)
