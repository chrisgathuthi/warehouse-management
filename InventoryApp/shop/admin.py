from pstats import StatsProfile
from django.contrib import admin

from .forms import StockAdminForms
from .models import Stock
# Register your models here.

@admin.action(description="Mark selected Stock as Cleared")
def make_cleared(modelAdmin,request,queryset):
    queryset.update(status="cleared")
    
class StockAdmin(admin.ModelAdmin):
    list_display = ["product_name","net_weight","qty","tags","status"]
    search_fields = ["product_name"]
    form = StockAdminForms
    actions =[make_cleared]

admin.site.register(Stock,StockAdmin)