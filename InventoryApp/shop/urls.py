
from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "shop"

urlpatterns =[
    path("",views.IndexView.as_view(),name="index"),
    path("stock-list-page/",views.StockList.as_view(),name="list-page"),
    path("dashboard/",views.Dashboard.as_view(),name="dashboard"),
    path("detail-page/<int:pk>/",views.StockDetail.as_view(),name="detail-page"),
    path("form-page/",views.StockCreate.as_view(),name="form-page")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)