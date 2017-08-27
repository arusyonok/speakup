from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.step_list),
    url(r'^([0-9]+)/exercise/([0-9]+)/$', views.exercise_detail),
]