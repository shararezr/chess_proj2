from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', home,name='home'),
    url(r'^login/',login, name='login'),
    url(r'^register_page/',register_page,name='register_page'),
    url(r'^register/',register,name='register'),
    url(r'^active_page/',active_page,name='active_page'),
    url(r'^chess_page/',chess_page,name='chess_page'),
    
    

]