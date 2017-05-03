from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView

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
		return reverse_lazy('backend.tip.edit', kwargs={'pk': self.object.pk})

	def get_context_data(self, **kwargs):
		data = super(TipCreateView, self).get_context_data(**kwargs)

		data['title_form'] = 'Add new Tip'

		return data


class TipUpdateView(UpdateView):
	model = Tip

	form_class = TipForm

	template_name = 'backend/tip/tip_form.html'

	context_object_name = 'tip'

	def get_success_url(self):
		return reverse_lazy('backend.tip.edit', kwargs={'pk': self.object.pk})

	def get_context_data(self, **kwargs):
		data = super(TipUpdateView, self).get_context_data(**kwargs)

		data['title_form'] = 'Update {0}'.format(self.object.title.title())

		message_tip = self.request.session.get('message_tip')

		if message_tip is not None:
			data['message_tip'] = message_tip

			self.request.session['message_tip'] = None

		return data

	def form_valid(self, form):
		form.save()

		self.request.session['message_tip'] = 'The tip has been saved successfully'

		return super(TipUpdateView, self).form_valid(form)


class TipDeleteView(View):
	def post(self, request):
		tip_id = request.POST.get('tip_id')

		tip_delete = Tip.get_by_id(tip_id)

		if tip_delete is not None:
			tip_delete.delete()

		return redirect(reverse('backend.tip.index'))
