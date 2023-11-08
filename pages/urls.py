from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('post', views.PostsListsView.as_view(), name= 'post_list'),
    path('post-detail/<int:pk>/', views.post_detail, name = 'post_detail'),
    path('post-new/', views.CreateNewPost.as_view(), name = 'post_new'),
    path('post-edit/<int:pk>/', views.UpdatePost.as_view(), name = 'post_edit'),
    path('post-delete/<int:pk>/', views.DeletePost.as_view(), name = 'post_delete'),
    path('', views.HomePage.as_view(), name= 'home_page'),
    path('about/', views.AboutPage.as_view(), name= 'about_page'),
    path('result/', views.SearchView.as_view(), name='post_search'),

]