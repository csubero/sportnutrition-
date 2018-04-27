import threading

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class EmailThread(threading.Thread):
	from_address = settings.DEFAULT_FROM_EMAIL
	template = 'website/email.html'

	def __init__(self,
				 subject,
				 recipient_list,
				 contact_info,
				 notification_email=None,
				 template='frontend/contact/email_template.html'):
		self.subject = subject
		self.recipient_list = recipient_list
		self.contact_info = contact_info
		self.template = template
		self.notification_email = notification_email

		threading.Thread.__init__(self)

	def run(self):
		print('Contact Info: ', self.contact_info)
		email_html = render_to_string(self.template, {"contact_info": self.contact_info})

		email = EmailMultiAlternatives(subject=self.subject,
									   body=email_html,
									   from_email=self.from_address,
									   to=self.recipient_list)

		email.attach_alternative(email_html, 'text/html')

		email.send()
