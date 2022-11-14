from io import BytesIO
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
# from .utils import render_to_pdf
from django.core.files import File
from datetime import datetime,timedelta
from .models import Stock

@receiver(post_save,sender=Stock)
def generate_obj_pdf(sender,instance,created,**kwargs):
    pass
    if created:
        obj = Stock.objects.get(id=instance.id)
        context = {'product_name': obj.product_name,"net_weight":obj.net_weight,"qty":obj.qty,"date":obj.date,"isle":obj.isle,"tags":obj.tags,"storage":obj.storage,"shelf_life":obj.shelf_life,"attendant":obj.attendant,"status":obj.status,"exp":obj.exp}
        pdf = render_to_pdf('shop/pdf.html', context)
        filename = f"{instance.product_name}_{instance.date}.pdf"
        obj.docs.save(filename, File(BytesIO(pdf.content)))

