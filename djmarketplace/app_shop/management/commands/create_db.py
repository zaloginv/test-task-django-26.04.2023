import lorem
import random
from django.core.management import BaseCommand
from app_shop.models import Shop, Product, ProductShop

class Command(BaseCommand):
    """
    Creates shops and products
    """
    def handle(self, *args, **options):
        self.stdout.write('---Creating shops---')

        number_of_shops = 7

        for _ in range(number_of_shops):
            shop_name = lorem.get_word(func='capitalize')
            shop_description = lorem.get_paragraph()
            shop_location = lorem.get_sentence()

            shop, created = Shop.objects.get_or_create(
                name=shop_name,
                description=shop_description,
                location=shop_location
            )

            self.stdout.write(f'Created: "{shop.name}"')

        self.stdout.write(self.style.SUCCESS('---All shops created---'))

        self.stdout.write('---Creating products---')

        number_of_products = 10

        for _ in range(number_of_products):
            product_name = lorem.get_word(func='capitalize')
            product_description = lorem.get_paragraph()

            product, created = Product.objects.get_or_create(
                name=product_name,
                description=product_description,
            )
                # product_shop, created = ProductShop.objects.get_or_create(
                #     quantity=random.randint(1, 20),
                #     price=random.randint(1_00, 10_000_00)/100,
                #     shop_id=shop_id,
                #     product_id=product.id
                # )

            self.stdout.write(f'Created: "{product.id}"')

        self.stdout.write(self.style.SUCCESS('---All products created---'))

        self.stdout.write('---Creating m2m product-shop connection---')

        for shop_id in range(1, number_of_shops+1):
            for product_id in range(1, number_of_products+1):
                product_shop, created = ProductShop.objects.get_or_create(
                    quantity=random.randint(1, 20),
                    price=random.randint(1_00, 10_000_00)/100,
                    shop_id=shop_id,
                    product_id=product_id
                )

                self.stdout.write(f'Created product with id: "{product_shop.product.id}"\n'
                                  f'in shop with id: "{product_shop.shop.id}"')

        self.stdout.write(self.style.SUCCESS('---All m2m connections created---'))