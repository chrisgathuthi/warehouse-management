
from django.urls import path

from . import views


app_name = "shop"

urlpatterns =[
    path("",views.IndexView.as_view(),name="index"),
    path("list-page/",views.StockList.as_view(),name="list-page"),
    path("dashboard/",views.Dashboard.as_view(),name="dashboard"),
    path("detail-page/<int:pk>/",views.StockDetail.as_view(),name="detail-page"),
    path("update/<int:pk>/",views.StockUpdate.as_view(),name="update-page"),
    path("form-page/",views.StockCreate.as_view(),name="form-page")
]
htmx_urlpatterns = [
    path("search/",views.search_product,name="search-product"),
]
urlpatterns += htmx_urlpatterns
