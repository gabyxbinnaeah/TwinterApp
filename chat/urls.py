from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views 
from django.urls import include 


urlpatterns =[
    url(r'^$',views.profile,name='homeUrl'),
    url('account/', include('django.contrib.auth.urls')),
    url('profile/<str:username>/',views.profile,name='profileUrl'),
    url('edit/profile/',views.update_profile,name='update'),
    url('image/',views.new_image,name='post'),
    url('search/', views.search_profile, name='search'),
    url('user_profile/<username>/', views.user_profile, name='user_profile'),
    url('unfollow/<to_unfollow>', views.unfollow, name='unfollow'),
    url('follow/<to_follow>', views.follow, name='follow'),
    url('image/<id>', views.comment, name='comment'),

    # url(r'^chat/image/$',views.new_image,name='new_image'),
]



urlpatterns=[
    path('',views.index,name = 'homeUrl'),
    path('account/', include('django.contrib.auth.urls')),
    path('profile/<str:username>/',views.profile,name='profile'),
    path('edit/profile/',views.update_profile,name='update'),
    path('image/',views.post,name='post'),
    path('search/', views.search_profile, name='search'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
    path('unfollow/<to_unfollow>', views.unfollow, name='unfollow'),
    path('follow/<to_follow>', views.follow, name='follow'),
    path('image/<id>', views.comment, name='comment'),
]