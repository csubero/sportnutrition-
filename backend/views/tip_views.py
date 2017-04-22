from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from backend.forms.tip_form import TipForm
from backend.models import Tip


class TipListView(ListView):
	model = Tip

	template_name = 'backend/tip/tip_index.html'

	context_object_name = 'tips_list'

	paginate_by = 10


class TipCreateView(CreateView):
	model = Tip

	form_class = TipForm

	template_name = 'backend/tip/tip_form.html'

	def get_success_url(self):
		return reverse_lazy('backend.tip.index')

	def get_context_data(self, **kwargs):
		data = super(TipCreateView, self).get_context_data(**kwargs)

		data['title_form'] = 'Add new Tip'

		return data
