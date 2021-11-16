from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$',                 views.TypeListView.as_view(), name='collapsed'),
    url(r'^(?P<stub>[-\w]+)$', views.TypeListView.as_view(), name='extended'),
    url(r'^pdf/(?P<pk>\d+)$',  views.document_view,          name='view-pdf'),
]


