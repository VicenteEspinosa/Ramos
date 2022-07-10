
from backend_app.db_urls.form_urls import form_urls
from backend_app.db_urls.location_urls import location_urls
from backend_app.db_urls.audit_urls import audit_urls
from backend_app.db_urls.technician_urls import technician_urls
from backend_app.db_urls.report_urls import report_urls
from backend_app.db_urls.form_tree_urls import form_tree_urls
from backend_app.db_urls.datalist_urls import metadata_lists_urls
from backend_app.db_urls.infodata_urls import infopanel_urls
from backend_app.db_urls.client_urls import clients_lists_urls
from backend_app.db_urls.dashboard_urls import dashboard_lists_urls

from django.contrib import admin
from django.urls import include, path

# Every url must end with a slash ( / )
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('backend_app.urls', 'users'), namespace='users')),
]

urlpatterns += form_urls
urlpatterns += location_urls
urlpatterns += audit_urls
urlpatterns += technician_urls
urlpatterns += report_urls
urlpatterns += form_tree_urls
urlpatterns += metadata_lists_urls
urlpatterns += infopanel_urls
urlpatterns += clients_lists_urls
urlpatterns += dashboard_lists_urls

