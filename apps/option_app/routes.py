from django.conf.urls import url
from . import views

urlpatterns = [    
    url(r'^$', views.sign_in_page),
    url(r'^register$',views.register),
    url(r'^login$',views.login),
    url(r'^create$',views.create),
    url(r'^logout$',views.logout),
    url(r'^create_page$', views.create_page),
    url(r'^dashboard$', views.dashboard),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^view_job/(?P<id>\d+)$', views.view_job),
    url(r'^edit/(?P<id>\d+)$', views.edit_job),
    url(r'^edit_job/(?P<id>\d+)$', views.edit_job),
    url(r'^view_job/(?P<id>\d+)/edit$', views.edit),

    
    


    

]