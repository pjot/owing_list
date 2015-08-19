from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/(?P<list_id>[0-9]+)$', views.trip, name='trip'),
    url(r'^settle/(?P<list_id>[0-9]+)$', views.settle, name='settle'),
    url(r'^add_person_to_list/(?P<list_id>[0-9]+)$', views.add_person_to_list, name='add_person'),
    url(r'^delete_person/(?P<person_id>[0-9]+)$', views.delete_person, name='delete_person'),
    url(r'^add_transaction/(?P<list_id>[0-9]+)$', views.add_transaction, name='add_transaction'),
    url(r'^add_payment$', views.add_payment, name='add_payment'),
    url(r'^delete_transaction/(?P<transaction_id>[0-9]+)$', views.delete_transaction, name='delete_transaction'),
    url(r'^add_list$', views.add_list, name='add_list'),
]
