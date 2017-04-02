from django.conf.urls import url

from backend.views import IndexView, PostListView, CategoryIndexView, CategoryDeleteView, PostCreateView, \
	PostUpdateView, PostDeleteView

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
]
