from django.conf.urls import url
from django.urls import path
from backend_app.db_views.report_view import (
    generate_report,
    generate_report_client_side,
    report_detail,
    report_list,
    report_for_api,
    reports_for_user_category,
    reports_by_category,
)


report_urls = [
    url('reports/', report_list),
    path('report/<pk>/', report_detail),
    path('generate_report/<pk>/', generate_report),
    path('generate_report_client_side/', generate_report_client_side),
    path('report_for_api/', report_for_api),
    path('reports_by_user_category/', reports_for_user_category),
    path('reports_by_category/<category>/', reports_by_category),
]
