from django.conf.urls import url, include
from .import views

app_name = 'Student_marks'

urlpatterns = [
   url(r'^$', views.index, name="index"),
   url(r'^extra/$', views.extra_view, name="extra_view"),

]