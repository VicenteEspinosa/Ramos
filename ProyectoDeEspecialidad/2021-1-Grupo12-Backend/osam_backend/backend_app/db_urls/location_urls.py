from django.conf.urls import url
from django.urls import path
from backend_app.db_views.region_view import (
    region_detail,
    region_list,
    region_list_indexed
)
from backend_app.db_views.province_view import (
    province_detail,
    province_list,
    province_list_indexed
)
from backend_app.db_views.commune_view import (
    commune_detail,
    commune_list,
    commune_list_indexed,
    commune_location
)

from backend_app.db_views.att_zone_view import (
    att_zone_list,
    att_zone_list_indexed,
    att_zone_detail
)

from backend_app.db_views.crmzone_view import (
    crmzone_list,
    crmzone_list_indexed,
    crmzone_detail,
)

location_urls = [
    url('communes/', commune_list),
    url('communes_indexed/', commune_list_indexed),
    path('commune/<pk>/', commune_detail),
    path('commune_location/<pk>/', commune_location),
    url('provinces/', province_list),
    url('provinces_indexed/', province_list_indexed),
    path('province/<pk>/', province_detail),
    url('regions/', region_list),
    url('regions_indexed/', region_list_indexed),
    path('region/<pk>/', region_detail),
    url('att_zones/', att_zone_list),
    url('att_zones_indexed/', att_zone_list_indexed),
    path('att_zone/<pk>/', att_zone_detail),
    url('crmzones/', crmzone_list),
    url('crmzones_indexed/', crmzone_list_indexed),
    path('crmzone/<pk>/', crmzone_detail),
]
