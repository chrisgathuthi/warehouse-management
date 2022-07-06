from shelve import Shelf
from django.core.management import BaseCommand
from shop.models import Stock
import os
file = os.path.basename("C:\\Users\\HP\\Downloads\\receipt.pdf")
#os.path.join("C:\\Users\\HP\Documents\\Dev\\presentation\\InventoryApp\\documents",file)
class Command(BaseCommand):
    help = "create 50 objects"
    def handle(self,*args, **options):
        for i in range(1000):
            u=Stock.objects.update_or_create(
                product_name="kasuku",
                net_weight= 3,
                qty= 11,
                isle=9,
                tags= "cereals",
                storage= "dry",
                shelf_life = "two years",
                status = "pending",
                docs= file
            )
        print("The process is complete")
    
