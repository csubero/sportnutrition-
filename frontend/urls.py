from django.conf.urls import url

from frontend.views import IndexTemporalView

urlpatterns = [
	url(r'^$', IndexTemporalView.as_view(), name='frontend.index'),
]
