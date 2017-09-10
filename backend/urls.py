from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from backend.views import IndexView, PostListView, CategoryIndexView, CategoryDeleteView, PostCreateView, \
	PostUpdateView, PostDeleteView, TipListView, TipCreateView, TipUpdateView, TipDeleteView, TipUploadImageView, \
	QuestionListView, QuestionCreateView

urlpatterns = [
	url(r'^$', IndexView.as_view(), name='backend.index'),

	# Category URL'S
	url(r'^categories/$', CategoryIndexView.as_view(), name='backend.category.index'),
	url(r'^categories/delete/$', CategoryDeleteView.as_view(), name='backend.category.delete'),

	# Post URL'S
	url(r'^posts/$', PostListView.as_view(), name='backend.post.index'),
	url(r'^posts/create/$', PostCreateView.as_view(), name='backend.post.create'),
	url(r'^posts/(?P<pk>[0-9]+)/edit/$', PostUpdateView.as_view(), name='backend.post.edit'),
	url(r'^posts/delete/$', PostDeleteView.as_view(), name='backend.post.delete'),

	# Tip URL'S
	url(r'^tips/$', TipListView.as_view(), name='backend.tip.index'),
	url(r'^tips/create/$', TipCreateView.as_view(), name='backend.tip.create'),
	url(r'^tips/(?P<pk>[0-9]+)/edit/$', TipUpdateView.as_view(), name='backend.tip.edit'),
	url(r'^tips/delete/$', TipDeleteView.as_view(), name='backend.tip.delete'),
	url(r'^tips/upload-image/$', TipUploadImageView.as_view(), name='backend.tip.upload_image'),

	# Question URL'S
	url(r'^question/$', QuestionListView.as_view(), name='backend.question.index'),
	url(r'^question/create/$', QuestionCreateView.as_view(), name='backend.question.create'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
