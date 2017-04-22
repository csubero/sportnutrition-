from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from backend.views import IndexView, PostListView, CategoryIndexView, CategoryDeleteView, PostCreateView, \
	PostUpdateView, PostDeleteView, TipListView, TipCreateView, TipUpdateView, TipDeleteView

urlpatterns = [
	url(r'^$', IndexView.as_view(), name='backend.index'),

	# Category URL'S
	url(r'^category/$', CategoryIndexView.as_view(), name='backend.category.index'),
	url(r'^category/delete/$', CategoryDeleteView.as_view(), name='backend.category.delete'),

	# Post URL'S
	url(r'^post/$', PostListView.as_view(), name='backend.post.index'),
	url(r'^post/create/$', PostCreateView.as_view(), name='backend.post.create'),
	url(r'^post/edit/(?P<pk>[0-9]+)/$', PostUpdateView.as_view(), name='backend.post.edit'),
	url(r'^post/delete/$', PostDeleteView.as_view(), name='backend.post.delete'),

	# Tip URL'S
	url(r'^tip/$', TipListView.as_view(), name='backend.tip.index'),
	url(r'^tip/create/$', TipCreateView.as_view(), name='backend.tip.create'),
	url(r'^tip/edit/(?P<pk>[0-9]+)/$', TipUpdateView.as_view(), name='backend.tip.edit'),
	url(r'^tip/delete/$', TipDeleteView.as_view(), name='backend.tip.delete'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
