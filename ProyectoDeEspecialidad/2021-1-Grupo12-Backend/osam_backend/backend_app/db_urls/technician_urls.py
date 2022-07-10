from django.conf.urls import url
from django.urls import path
from backend_app.db_views.team_view import (
    team_list,
    team_list_indexed,
    team_detail
)
from backend_app.db_views.technician_view import (
    technician_detail,
    technician_list,
    technician_list_indexed,
    technician_by_category,
    technician_indexed_by_category,
    technician_list_paginated
)
from backend_app.db_views.enterprise_view import (
    enterprise_detail,
    enterprise_list,
    enterprise_list_indexed
)


technician_urls = [
    url('technicians/', technician_list),
    url('technicians_indexed/', technician_list_indexed),
    url('technicians_paginated/', technician_list_paginated),
    path('technicians_by_category/<category_id>/', technician_by_category),
    path('technicians_indexed_by_category/<category_id>/', technician_indexed_by_category),
    path('technician/<pk>/', technician_detail),
    url('enterprises/', enterprise_list),
    path('enterprise/<pk>/', enterprise_detail),
    url('enterprises_indexed/', enterprise_list_indexed),
    url('teams/', team_list),
    url('teams_indexed/', team_list_indexed),
    path('team/<pk>/', team_detail),
]
