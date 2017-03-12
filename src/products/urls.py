from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.ProductListView.as_view(), name='product_list'),    
    url(r'^categories/$', views.CategoryListView.as_view(), name='category_list'),
    url(r'^categories/(?P<slug>[\w-]+)/$', views.CategoryDetail.as_view(), name='category_detail'),
    url(r'^(?P<id>[\w-]+)/$', views.ProductDetailView.as_view(), name='product_detail'),
    url(r'^(?P<id>[\w-]+)/variation/?', views.VariationListView.as_view(), name='variation_list'),
]
