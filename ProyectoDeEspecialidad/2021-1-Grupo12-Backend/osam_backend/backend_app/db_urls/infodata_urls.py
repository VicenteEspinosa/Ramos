
from backend_app.db_views.infopanel_view import (
    info_panel_indexed,
    infopaneldata_detail)

from django.conf.urls import url
from django.urls import path

infopanel_urls = [
    url('infopanel/', info_panel_indexed),
    path('infodata/<pk>/', infopaneldata_detail)
]