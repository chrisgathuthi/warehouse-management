from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from . import views
urlpatterns = [
    path("create-stock/",views.StockCreateView.as_view(),name="create-stock-api"),
    path("list-stock/",views.StockListView.as_view(),name="list-stock-api"),
    path("update-stock/<int:pk>/",views.StockUpdateView.as_view(),name="update-stock-api"),
    path("get-stock/<int:pk>/",views.StockUpdateView.as_view(),name="stock-retrieve-api"),
    path("delete-stock/<int:pk>/",views.StockDeleteView.as_view(),name="delete-stock-api"),
    path("user/",views.UserListView.as_view(),name="user-list-api"),
    path("user/<int:pk>/",views.UserDetailView.as_view(),name="user-get-api"),
    path("auth/",obtain_auth_token),
    
]
urlpatterns = format_suffix_patterns(urlpatterns)