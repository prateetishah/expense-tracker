from django.urls import path
from . import views
from expense_tracker_1 import settings
from django.conf.urls.static import static
urlpatterns =[
path("", views.import_excel_pandas, name="import_excel_pandas"),
path('import_excel_pandas/', views.import_excel_pandas, name="import_excel_pandas"),
path('import_excel', views.import_excel, name="import_excel"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)