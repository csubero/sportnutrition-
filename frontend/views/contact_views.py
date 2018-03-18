from django.urls import reverse
from django.views.generic import FormView

from frontend.forms import ContactForm


class ContactView(FormView):
	template_name = 'frontend/contact/contact_form.html'

	form_class = ContactForm

	def get_success_url(self):
		return reverse('frontend.index.index')

	def form_valid(self, form):
		form.send_mail()

		return super(ContactView, self).form_valid(form)
