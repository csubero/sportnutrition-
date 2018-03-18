from django import forms

from sportnutrition.libraries.email_interface import EmailThread


class ContactForm(forms.Form):
	name = forms.CharField(max_length=100)
	email = forms.EmailField(max_length=255)
	message = forms.CharField(widget=forms.Textarea())

	def send_mail(self):
		EmailThread(subject='New Contact Info',
					recipient_list=['info@sportnutrition.com'],
					contact_info=self.cleaned_data).start()
