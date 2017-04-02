from django.conf.urls import url

from backend.views import IndexView
from backend.views.category_views import CategoryIndexView, CategoryDeleteView

urlpatterns = [
	url(r'^$', IndexView.as_view(), name='backend.index'),

	# Category URL'S
	url(r'^category/$', CategoryIndexView.as_view(), name='backend.category.index'),
	url(r'^category/delete/$', CategoryDeleteView.as_view(), name='backend.category.delete'),
]
