from django.conf.urls import include, url
from django.contrib import admin

from dashboard.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login$', login, name='login'),
    url(r'^logout$', logout, name='logout'),
    url(r'^encomendas$', orders, name='orders'),
    url(r'^encomenda/nova$', new_order, name='new_order'),
    url(r'^encomenda/editar/(?P<id_order>\d+)/$', edit_order, name='edit_order'),
    url(r'^encomenda/remover/(?P<id_order>\d+)/$', rmv_order, name='rmv_order'),
    url(r'^clientes$', clients, name='clients'),
    url(r'^cliente/novo$', new_client, name='new_client'),
    url(r'^cliente/editar/(?P<id_client>\d+)/$', edit_client, name='edit_client'),
    url(r'^cliente/remover/(?P<id_client>\d+)/$', rmv_client, name='rmv_client'),
    url(r'^faturamento$', billing, name='billing'),
    url(r'^produtos$', products, name='products'),
    url(r'^produto/novo$', new_product, name='new_product'),
    url(r'^produto/editar/(?P<id_product>\d+)/$', edit_product, name='edit_product'),
    url(r'^produto/remover/(?P<id_product>\d+)/$', rmv_product, name='rmv_product'),
    url(r'^admin/', include(admin.site.urls)),
]
