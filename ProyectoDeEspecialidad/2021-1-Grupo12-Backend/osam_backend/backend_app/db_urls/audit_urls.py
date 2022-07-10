from django.conf.urls import url
from django.urls import path
from backend_app.db_views.answer_view import (
    answer_detail,
    answer_list,
    answer_list_indexed,
    answer_loader,
    answer_list_paginated
)


audit_urls = [
    url('answers/', answer_list),
    url('answers_indexed/', answer_list_indexed),
    path('answer/<pk>/', answer_detail),
    url('answers_loader/', answer_loader),
    url('answers_paginated/', answer_list_paginated),
]
