from django.conf.urls import url 

from tango_with_django_project import views

urlpatterns = [
    url(r'^$', views.index, name='index'), 

    ]