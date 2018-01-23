
from django.conf.urls import url
from polls import views
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^booklist/$', views.booklist, name='booklist')

]
