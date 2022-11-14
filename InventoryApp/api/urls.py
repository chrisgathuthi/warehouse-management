from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
urlpatterns = [
    path("create_stock/",views.StockCreateView.as_view(),name="create-stock-api"),
    path("list_stock/",views.StockListView.as_view(),name="list-stock-api"),
    path("update_stock/<int:pk>/",views.StockUpdateView.as_view(),name="update-stock-api"),
    path("delete_stock/<int:pk>/",views.StockDeleteView.as_view(),name="delete-stock-api"),
    
]
urlpatterns = format_suffix_patterns(urlpatterns)