from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path

from backend.views import IndexView, PostListView, CategoryIndexView, CategoryDeleteView, PostCreateView, \
	PostUpdateView, PostDeleteView, TipListView, TipCreateView, TipUpdateView, TipDeleteView, TipUploadImageView, \
	QuestionListView, QuestionCreateView

urlpatterns = [
	path('', IndexView.as_view(), name='backend.index'),

	# Category URL'S
	path('categories/', CategoryIndexView.as_view(), name='backend.category.index'),
	path('categories/delete/', CategoryDeleteView.as_view(), name='backend.category.delete'),

	# Post URL'S
	path('posts/', PostListView.as_view(), name='backend.post.index'),
	path('posts/create/', PostCreateView.as_view(), name='backend.post.create'),
	path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='backend.post.edit'),
	path('posts/delete/', PostDeleteView.as_view(), name='backend.post.delete'),

	# Tip URL'S
	path('tips/', TipListView.as_view(), name='backend.tip.index'),
	path('tips/create/', TipCreateView.as_view(), name='backend.tip.create'),
	path('tips/<int:pk>/edit/', TipUpdateView.as_view(), name='backend.tip.edit'),
	path('tips/delete/', TipDeleteView.as_view(), name='backend.tip.delete'),
	path('tips/upload-image/', TipUploadImageView.as_view(), name='backend.tip.upload_image'),

	# Question URL'S
	path('question/', QuestionListView.as_view(), name='backend.question.index'),
	path('question/create/', QuestionCreateView.as_view(), name='backend.question.create'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
