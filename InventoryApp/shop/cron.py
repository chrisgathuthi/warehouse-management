from datetime import date
from .models import Stock
def check_status():
    obj = Stock.objects.all()
    for qs in obj:
        if qs.exp <= date.today():
            qs.status= "Expired"
            qs.save()
    return None

    