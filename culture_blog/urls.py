from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.BlogPostList.as_view(), name='blog_home'),
    path('', views.index, name='index'),
    path('<int:pk>/', views.single_post, name='post_details'),
    path('tools/', views.tools, name='tools'),
    # path('details/(?P<pk>\d+)', views.BlogPostDetails.as_view(), name='post_details'),

]
