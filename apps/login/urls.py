from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='login_index'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^helloworld$', views.hello_world, name="hellowolrd")
]