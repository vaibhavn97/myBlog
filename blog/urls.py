from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('post/new', views.PostCreateView.as_view(), name='post-new'),
    path('post/update/<int:pk>', views.PostUpdateView.as_view(), name='post-update'),
    path('post/delete/<int:pk>', views.PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>', views.post_detail, name='post')
]