from django.conf.urls import url
from django.urls import path
from backend_app.db_views.form_view import (
    form_detail,
    form_list,
    form_list_indexed
)
from backend_app.db_views.block_view import (
    block_delete,
    block_detail,
    block_list,
    block_list_indexed,
    block_associated_forms,
    block_list_category_for_form,
)
from backend_app.db_views.question_view import (
    question_delete,
    question_detail,
    question_list,
    question_list_active,
    question_list_active_indexed,
    question_list_category,
    question_list_indexed,
    question_associated_blocks,
    question_list_active_paginated
)


form_urls = [
    url('questions/', question_list),
    url('questions_indexed/', question_list_indexed),
    url('questions_active_paginated/', question_list_active_paginated),
    url('questions_active/', question_list_active),
    url('questions_active_indexed/', question_list_active_indexed),
    path('question/<pk>/', question_detail),
    path('questions_category/<category>/', question_list_category),
    path('question_delete/<pk>/', question_delete),
    path('question_associated_blocks/<pk>/', question_associated_blocks),
    url('blocks/', block_list),
    url('blocks_indexed/', block_list_indexed),
    path('block/<pk>/', block_detail),
    path('block_delete/<pk>/', block_delete),
    path('block_associated_forms/<pk>/', block_associated_forms),
    path('block_category_for_form/<category>/<for_form>/', block_list_category_for_form),
    url('forms/', form_list),
    url('forms_indexed/', form_list_indexed),
    path('form/<pk>/', form_detail)
]
