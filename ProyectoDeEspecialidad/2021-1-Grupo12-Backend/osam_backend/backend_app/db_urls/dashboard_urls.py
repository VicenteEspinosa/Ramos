from django.conf.urls import url
from django.urls import path
from backend_app.db_views.dashboard_view import (
    get_dashboard
)


dashboard_lists_urls = [
    url('dashboard/', get_dashboard),
]
