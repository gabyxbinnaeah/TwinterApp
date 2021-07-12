from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views 

urlpatterns =[
    url(r'^$',views.profile,name='homeUrl'),
    url(r'^chat/image/$',views.new_image,name='new_image')
]