
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = "shop"

urlpatterns =[
    path("",views.IndexView.as_view(),name="index"),
    path("list-page/",views.StockList.as_view(),name="list-page"),
    path("dashboard/",views.Dashboard.as_view(),name="dashboard"),
    path("detail-page/<int:pk>/",views.StockDetail.as_view(),name="detail-page"),
    path("update/<int:pk>/",views.StockUpdate.as_view(),name="update-page"),
    path("form-page/",views.StockCreate.as_view(),name="form-page"),

    path('pdf/', views.Pdfs.as_view(),name="pdfs"),

    path('login/', auth_views.LoginView.as_view(),name="login"),
    path("logout/",views.StockLogout,name="logout-page"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
htmx_urlpatterns = [
    path("search/",views.search_product,name="search-product"),
    path("timer/",views.Timer.as_view(),name="base-html"),
]
urlpatterns += htmx_urlpatterns

