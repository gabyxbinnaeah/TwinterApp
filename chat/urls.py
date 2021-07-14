from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name = 'index'),
    path('account/', include('django.contrib.auth.urls')),
    path('profile/<str:username>/',views.profile_user,name='profile'),
    path('edit/profile/',views.update_user_profile,name='update'),
    path('image/',views.post,name='post'),
    path('search/', views.search_user_profile, name='search'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
    path('unfollow/<to_unfollow>', views.unfollow_user, name='unfollow'),
    path('follow/<to_follow>', views.follow_user, name='follow'),
    path('image/<id>', views.comment, name='comment'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

