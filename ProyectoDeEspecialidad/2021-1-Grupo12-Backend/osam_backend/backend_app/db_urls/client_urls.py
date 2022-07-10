from django.conf.urls import url
from django.urls import path
from backend_app.db_views.client_view import (
    client_list,
    client_detail
)


clients_lists_urls = [
    url('clients/', client_list),
    path('client/<pk>/', client_detail)
]
