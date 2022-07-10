from django.conf.urls import url
from django.urls import path
from backend_app.db_views.form_tree_view import ( 
    edit_del_category, 
    get_form_tree, 
    get_post_category, 
    post_form_tree,
    put_activate_category,
    del_inactive_category,
    get_active_tree
)


form_tree_urls = [
    url('categories/', get_post_category),
    url('form_tree/active/', get_active_tree),
    url('form_tree/', get_form_tree),
    url('form_tree_new/', post_form_tree),
    path('category/<pk>/', edit_del_category),
    path('category/activate/<pk>/', put_activate_category),
    path('category/inactive/<pk>/', del_inactive_category)
]
