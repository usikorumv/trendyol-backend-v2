import ujson
from slugify import slugify
from .trendyol_scraper import TrendyolScraper
from base_product.models import *
from products.models import *
from product_cards.models import *

# TODO: PASTE ALL SLUGS FROM SLUGIFY


class Scraper:
    def __init__(self):
        self.scraper = TrendyolScraper()

    def parse_colors(self):
        Color.objects.all().delete()

        all_colors = self.scraper.get_all_colors()

        for color in all_colors:
            name = color["name"]
            slug = color["slug"]
            Color.objects.update_or_create(slug=slug, defaults={"color": name})

        return f"Colors were added successfully! {len(all_colors)}"

    def parse_brands(self):
        Brand.objects.all().delete()

        all_brands = self.scraper.get_all_brands()

        for brand in all_brands:
            name = brand["name"]
            slug = brand["slug"]
            Brand.objects.update_or_create(slug=slug, defaults={"brand": name})

        return f"Brands were added successfully {len(all_brands)}"

    def parse_sizes(self):
        Size.objects.all().delete()

        all_sizes = self.scraper.get_all_sizes()

        for size in all_sizes:
            name = size["name"]
            slug = size["slug"]
            Size.objects.update_or_create(slug=slug, defaults={"name": name})

        return f"Sizes added successfully! {len(all_sizes)}"

    def parse_categories(self):
        Category.objects.all().delete()

        all_categories = self.scraper.get_all_categories()

        for category in all_categories:
            name = category["name"]
            slug = category["slug"]

            try:
                parent = category["parent"]
                parent = Category.objects.get(slug=parent)
                Category.objects.update_or_create(
                    slug=slug, defaults={"title": name, "parent": parent}
                )
            except:
                Category.objects.update_or_create(slug=slug, defaults={"title": name})

        return f"Categories were added successfully! {len(all_categories)}"

    def parse_product_cards(self, currency="TL", coefficient=1):
        all_product_cards = self.scraper.get_all_product_cards()

        # FOR TEST PURPOSES
        # with open("output/products.json", "r", encoding="utf-8") as f:
        #     all_product_cards = ujson.load(f)

        for product_card in all_product_cards:
            print(product_card["id"])

            product_card_obj = self.add_product_to_db(product_card, ProductCard)

            for color in product_card["colors"]:
                color_obj = Color(name=color["name"], slug=color["slug"])
                color_obj.save()

                product_obj = self.add_product_to_db(color["product"], Product)

                ProductColor.objects.update_or_create(color=color_obj, product_card=product_card_obj, product=product_obj)


    def add_product_to_db(self, product, instance: BaseProduct) -> BaseProduct:
        image_urls = product["images"]
        category = product["category"]
        show_color = product["showColor"]
        show_size = product["showSize"]
        brand = product["brand"]
        sizes = product["sizes"]

        try:
            category_obj = Category.objects.get(slug=category["slug"])
        except:
            category_obj = Category(slug=category["slug"], title=category["name"])
            category_obj.save()

        brand_obj = Brand(name=brand["name"], slug=brand["slug"])
        brand_obj.save()

        color_obj = Color(name=show_color, slug=slugify(show_color))
        color_obj.save()

        size_obj = Size(name=show_size, slug=slugify(show_size))
        size_obj.save()

        product_obj = instance(
            id=product["id"],
            campaign=product["campaign"],
            name=product["name"],
            rating=product["rating"],
            description=product["description"],
            category=category_obj,
            show_color=color_obj,
            show_size=size_obj,
            discounted_price=product["price"]["discountedPrice"]["value"],
            selling_price=product["price"]["sellingPrice"]["value"],
            original_price=product["price"]["originalPrice"]["value"],
            currency=product["price"]["currency"],
            brand=brand_obj,
        )
        product_obj.save()

        for url in image_urls:
            Image.objects.update_or_create(url=url, product=product_obj)

        for size in sizes:
            size_obj = Size(name=size["value"], slug=slugify(size["value"]))
            size_obj.save()
            ProductSize.objects.update_or_create(size=size_obj, in_stock=size["inStock"], product=product_obj,
                                                 price=size["price"])

        return product_obj
