from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^{id}$', views.viewEvent, name='view_Event'),
    url(r'^create$', views.createEvent, name='create_Event'),
    url(r'^new$', views.newEvent, name='new_Event'),
]