from django.urls import re_path, path
from . import views
app_name = "polls"

urlpatterns = [

    re_path(r'^$', views.index, name="index"),
    #127.0.0.1/polls/
    re_path(r'^(?P<question_id>[0-9]+)/$', views.detail, name="detail"),
    #127.0.0.1/polls/1
    re_path(r'^(?P<question_id>[0-9]+)/results$', views.results, name="results"),
    # 127.0.0.1/polls/1/results
    re_path(r'^(?P<question_id>[0-9]+)/vote$', views.vote, name="vote"),
    # 127.0.0.1/polls/1/vote
]