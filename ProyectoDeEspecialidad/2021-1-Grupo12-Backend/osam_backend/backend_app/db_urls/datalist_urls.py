from django.conf.urls import url
from django.urls import path
from backend_app.db_views.datalist_view import (
    datalist,
    vehicles,
    task_types,
    non_ok_options,
)

metadata_lists_urls = [
    url('datalist/', datalist),
    url('vehicles/', vehicles),
    url('task_types/', task_types), 
    url('non_ok_options/', non_ok_options)
]
