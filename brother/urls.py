from django.conf.urls import url

from . import views

app_name = 'brother'

urlpatterns = [
    url(r'^$', views.all_family.as_view(), name='all_family'),
    url(r'^home/$', views.all_home.as_view(), name='all_home'),
    url(r'^not_home/$', views.all_not_home.as_view(), name='all_not_home'),
    url(r'^in/(?P<mac_address>([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})+)/$', views.checking_in, name='checking_in'),
    url(r'^out/(?P<mac_address>([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})+)/$', views.checking_out, name='checking_out')
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

# urlpatterns = [
#     url(r'^$', views.IndexView.as_view(), name='index'),
#     url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
#     url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
#     url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
# ]