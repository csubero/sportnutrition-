from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from frontend.views import IndexTemporalView, IndexView, PostDetailView

urlpatterns = [
	url(r'^$', IndexTemporalView.as_view(), name='frontend.index'),
	url(r'^home/$', IndexView.as_view(), name='frontend.index.index'),

	# Posts URL'S
	url(r'^post/(?P<slug>[\w-]+)/$', PostDetailView.as_view(), name='frontend.post.detail'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
