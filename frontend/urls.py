from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from frontend.views import IndexTemporalView, IndexView, PostDetailView, PostIndexView, AboutPageView, SearchView, \
	QuestionnaireView

urlpatterns = [
	# url(r'^$', IndexTemporalView.as_view(), name='frontend.index'),
	url(r'^$', IndexView.as_view(), name='frontend.index.index'),

	# Posts URL'S
	url(r'^posts/$', PostIndexView.as_view(), name='frontend.post.index'),
	url(r'^post/(?P<slug>[\w-]+)/$', PostDetailView.as_view(), name='frontend.post.detail'),

	# Mixing Pages
	url(r'^about-us/$', AboutPageView.as_view(), name='frontend.pages.about'),
	url(r'^search/$', SearchView.as_view(), name='frontend.search.result'),

	# Questionnaire URL'S
	url(r'^questionnaire/$', QuestionnaireView.as_view(), name='frontend.questionnaire.index'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
