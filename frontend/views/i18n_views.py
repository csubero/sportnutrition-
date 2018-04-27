from django.conf import settings
from django.utils import translation
from django.views import View
from django import http
from django.utils.translation import ugettext_lazy as _


class SetLanguage(View):
	ENGLISH = 'en'
	SPANISH = 'es'

	LANGUAGES = [
		(ENGLISH, _('English')),
		(SPANISH, _('Spanish')),
	]

	def get(self, request, lang):

		if lang == self.ENGLISH or lang == self.SPANISH:

			translation.activate(lang)
			response = http.HttpResponse()
			response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)
