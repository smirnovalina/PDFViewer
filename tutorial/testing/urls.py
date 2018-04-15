from django.conf.urls import url
from django.views.generic.base import TemplateView
from testing import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^test/$', views.TestList.as_view(), name='test'),
    url(r'^test/(?P<pk>[0-9]+)/$', views.TestDetail.as_view()),
    url(r'^result/$', views.ResultList.as_view(), name='result'),
    url(r'^result/(?P<pk>[0-9]+)/$', views.ResultDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]
