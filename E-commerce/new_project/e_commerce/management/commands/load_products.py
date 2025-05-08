import json
import uuid
from django.core.management.base import BaseCommand
from e_commerce.models import Product

class Command(BaseCommand):
    help = 'Load products from products.json into the database'

    def handle(self, *args, **kwargs):
        # Path to your JSON file
        with open(r'C:\Users\seife\OneDrive\Desktop\venv2\new_project\new_project\products_updated.json', 'r') as file:
            data = json.load(file)

            for product_data in data:
                product_id = product_data.get('id', str(uuid.uuid4()))  # In case the ID is missing
                product, created = Product.objects.get_or_create(
                    id=product_id,
                    defaults={
                        'category': product_data['category'],
                        'name': product_data['name'],
                        'seller': product_data['seller'],
                        'price': product_data['price'],
                        'stock': product_data['stock'],
                        'ratings': product_data['ratings'],
                        'ratingsCount': product_data['ratingsCount'],
                        'img': product_data['img'],
                        'shipping': product_data['shipping'],
                        'quantity': product_data['quantity'],
                    }
                )
                if created:
                    self.stdout.write(f"Added product: {product.name}")
                else:
                    self.stdout.write(f"Updated product: {product.name}")
