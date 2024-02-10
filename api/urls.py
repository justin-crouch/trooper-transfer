from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.Home.as_view(), name='home'),
	path('about/', views.AboutView.as_view(), name='about'),

	# Load specific posts depending on which thread is being accessed
	path('army/', views.PostList.as_view(thread=0, template_name='api/army_list.html'), name='army'),
	path('tech/', views.PostList.as_view(thread=1, template_name='api/tech_list.html'), name='tech'),
	
	# Load a specific post, if available
	path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]