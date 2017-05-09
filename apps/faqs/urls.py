from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^categories/$', views.FaqCategoryListView.as_view(), name='category_list'),
    url(r'^categories/(?P<slug>[\w-]+)/$', views.FaqCategoryView.as_view(), name='category'),
    url(r'^$', views.FaqListView.as_view(), name='faq_list'),
    url(r'^(?P<slug>[\w-]+)/$', views.FaqView.as_view(), name='faq'),
]
