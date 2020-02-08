from django.urls import re_path,path
from . import views
app_name = 'blog'

urlpatterns = [
    re_path(r'^$', views.PostListView.as_view(), name='post_lists'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
    views.post_detail,
    name='post_detail'),
    
    
]
