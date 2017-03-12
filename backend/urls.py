from django.conf.urls import url

from backend.views import IndexView

urlpatterns = [
	url(r'^$', IndexView.as_view(), name='backend.index'),
]
