from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from frontend.views import *

urlpatterns = [
	# url(r'^$', IndexTemporalView.as_view(), name='frontend.index'),
	path('', IndexView.as_view(), name='frontend.index.index'),

	# Posts URL'S
	path('posts/', PostIndexView.as_view(), name='frontend.post.index'),
	path('post/<slug:slug>/', PostDetailView.as_view(), name='frontend.post.detail'),

	# Mixing Pages
	path('about-us/', AboutPageView.as_view(), name='frontend.pages.about'),
	path('search/', SearchView.as_view(), name='frontend.search.result'),

	# Questionnaire URL'S
	path('questionnaire/', QuestionnaireView.as_view(), name='frontend.questionnaire.index'),

	# Contact URL'S
	path('contact-us/', ContactView.as_view(), name='frontend.contact_us'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
