from io import BytesIO
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .utils import render_to_pdf
from django.core.files import File
from datetime import datetime,timedelta
from .models import Stock

@receiver(post_save,sender=Stock)
def generate_obj_pdf(sender,instance,created,**kwargs):
    if created:
        obj = Stock.objects.get(id=instance.id)
        context = {'product_name': obj.product_name,"net_weight":obj.net_weight,"qty":obj.qty,"date":obj.date,"isle":obj.isle,"tags":obj.tags,"storage":obj.storage,"shelf_life":obj.shelf_life,"attendant":obj.attendant,"status":obj.status,"exp":obj.exp}
        pdf = render_to_pdf('shop/pdf.html', context)
        filename = f"{instance.product_name}_{instance.date}.pdf"
        obj.docs.save(filename, File(BytesIO(pdf.content)))

@receiver(pre_save,sender=Stock)
def modify_prams(sender,instance,**kwargs):
    if instance.tags == "cereals":
        instance.storage = "dry"
        instance.exp = datetime.now() + timedelta(days=20)

    if instance.tags == "dairy":
        instance.storage = "freezer"
        instance.exp = datetime.now() + timedelta(days=9)

    if instance.tags == "flour":
        instance.storage = "air_tight"
        instance.exp = datetime.now() + timedelta(days=6)

    if instance.tags == "fat_oils":
        instance.storage = "low"
        instance.exp = datetime.now() + timedelta(days=3)

    if instance.tags == "cereals" or instance.tags == "flour":
        instance.shelf_life = "less than six months"

    elif instance.tags == "dairy" or instance.tags == "fat_oils":
        instance.shelf_life = "less than three months"
    #instance.save()