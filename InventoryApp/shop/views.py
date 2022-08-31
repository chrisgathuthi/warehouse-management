
from typing import Dict
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView,DetailView,ListView,UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from .models import Stock
from .forms import StockForm
from django.db.models import Q
# Create your views here.


# @method_decorator(login_required,name="dispatch")
class IndexView(TemplateView):
    template_name = "index.html"

class Dashboard(TemplateView):
    template_name = "shop/dashboard.html"

class StockList(ListView):
    template_name = "shop/shop_list.html"
    model = Stock
    paginate_by = 50
    #queryset = Stock.objects.all()
    context_object_name = "shop_lists"

class StockDetail(DetailView):
    template_name = "shop/shop_detail.html"
    model = Stock
    context_object_name = "shop_detail"

class StockCreate(LoginRequiredMixin,CreateView):
    model = Stock
    form_class = StockForm
    template_name = "shop/stock_form.html"
    success_url = reverse_lazy("shop:detail-page")
    

    def get_initial(self) -> Dict:
        initial = super().get_initial()
        initial["attendant"]= self.request.user
        initial["status"] = "pending"
        return initial
    def form_valid(self, form) -> HttpResponse:
        form.instance.attendat = self.request.user
        return super().form_valid(form)

  
class StockUpdate(UpdateView):
    model = Stock
    template_name = "shop/shop_update.html"
    form_class = StockForm
    success_url = reverse_lazy("shop:detail-page")


def search_product(request):
    q = request.POST["productname"]
    if q is not None or q != "":
        q_results = Stock.objects.filter(Q(product_name__icontains="q") | Q(status__icontains="q"))
        return render(request,"partial/search-results.html",{"q_results":q_results})

    
