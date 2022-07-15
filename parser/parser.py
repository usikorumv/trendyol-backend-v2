from products.models import *
from trendyol_scraper import TrendyolScraper

import json
from django.db.utils import IntegrityError
import os.path

class Scraper:
    def __init__(self):
        self.scraper = TrendyolScraper()

    def parse_colors(self):
        Color.objects.all().delete()

        colors = self.scraper.get_all_colors()

        for color in colors:
            name = color["name"]
            slug = color["slug"]
            Color.objects.update_or_create(slug=slug, defaults={"color": name})

        return f"Colors were added successfully! {len(colors)}"

    def parse_brands(self):
        Brand.objects.all().delete()

        brands = self.scraper.get_all_brands()

        for brand in brands:
            name = brand["name"]
            slug = brand["slug"]
            Brand.objects.update_or_create(slug=slug, defaults={"brand": name})

        return f"Brands were added successfully {len(brands)}"

    def parse_sizes(self):
        Size.objects.all().delete()

        sizes = self.scraper.get_all_sizes()

        for size in sizes:
            name = size["name"]
            slug = size["slug"]
            Size.objects.update_or_create(slug=slug, defaults={"name": name})

        return f"Sizes added successfully! {len(sizes)}"

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

            # if category.get("parent", "") != "":
            #     Category.objects.update_or_create(slug=slug, defaults={"title": name})
            # else:
            #     parent = category["parent"]
            #     parent = Category.objects.get(slug=parent)
            #     Category.objects.update_or_create(
            #         slug=slug, defaults={"title": name, "parent": parent}
            #     )

        return f"Categories were added sucessfully! {len(all_categories)}"

    def parse_products(self, coefficient):
        Product.objects.all().delete()

        all_products = self.scraper.get_all_products()

        for product in all_products:
            id = product["id"]
            name = product["name"]
            campaign = product["campaign"]
            discounted_price = product["price"]["discountedPrice"]["value"]
            selling_price = product["price"]["sellingPrice"]["value"]
            original_price = product["price"]["originalPrice"]["value"]
            currency = product["price"]["currency"]
            description = product["description"]
            brand_slug = product["brand"]["slug"]

            try:
                brand = Brand.objects.get(slug=brand_slug)
            except:
                Brand.objects.create(slug=brand_slug, brand=brand_slug)
                brand = Brand.objects.get(slug=brand_slug)
            color_slug = product["showColor"]
            try:
                color = Color.objects.get(slug=color_slug)
            except:
                Color.objects.create(slug=color_slug, color=color_slug)
                color = Color.objects.get(slug=color_slug)
            category_slug = product["category"]["slug"]
            try:
                category = Category.objects.get(slug=category_slug)
            except:
                Category.objects.create(slug=category_slug, title=category_slug)
                category = Category.objects.get(slug=category_slug)
            show_size_slug = product["showSize"].lower()
            try:
                show_size = Size.objects.get(slug=show_size_slug)
            except:
                Size.objects.create(slug=show_size_slug, name=show_size_slug.upper())
                show_size = Size.objects.get(slug=show_size_slug)
            try:
                Product.objects.create(
                    id=id,
                    name=name,
                    # link=link,
                    description=description,
                    category=category,
                    discounted_price=discounted_price * coefficient,
                    selling_price=selling_price * coefficient,
                    original_price=original_price * coefficient,
                    brand=brand,
                    campaign=campaign,
                    currency=currency,
                    color=color,
                    show_size=show_size,
                )
            except IntegrityError:
                pass

            all_sizes = product["sizes"]
            product_obj = Product.objects.get(pk=id)
            images_list = product["images"]

            for image_url in images_list:
                Image.objects.get_or_create(product=product_obj, image=image_url)

            # reviews = product["reviews"]
            # Rating.objects.filter(product=product_obj).delete()
            # for review in reviews:
            #     author = review["user"]
            #     rate = review["rate"]
            #     comment = review["comment"]
            #     date = review["date"]
            #     Rating.objects.create(product=product_obj,author=author, rating=rate, created_at=date, comment=comment)

            for size in all_sizes:
                value_slug = size["value"].lower()
                try:
                    value = Size.objects.get(slug=value_slug)
                except:
                    Size.objects.create(slug=value_slug, name=value_slug.upper())
                    value = Size.objects.get(slug=value_slug)
                in_stock = size["inStock"]
                price = size["price"]
                currency = size["currency"]
                
            colors = product["colors"]
            for product_color in colors:
                id = product_color["product"]["id"]
                name = product_color["product"]["name"]
                campaign = product_color["product"]["campaign"]
                discounted_price = product_color["product"]["price"]["discountedPrice"][
                    "value"
                ]
                selling_price = product_color["product"]["price"]["sellingPrice"][
                    "value"
                ]
                original_price = product_color["product"]["price"]["originalPrice"][
                    "value"
                ]
                currency = product_color["product"]["price"]["currency"]
                description = product_color["product"]["description"]
                brand_slug = product_color["product"]["brand"]["slug"]
                try:
                    brand = Brand.objects.get(slug=brand_slug)
                except:
                    Brand.objects.create(slug=brand_slug, brand=brand_slug)
                    brand = Brand.objects.get(slug=brand_slug)
                color_slug = product_color["slug"]
                try:
                    color = Color.objects.get(slug=color_slug)
                except:
                    Color.objects.create(slug=color_slug, color=color_slug)
                    color = Color.objects.get(slug=color_slug)
                category_slug = product_color["product"]["category"]["slug"]
                try:
                    category = Category.objects.get(slug=category_slug)
                except:
                    Category.objects.create(slug=category_slug, title=category_slug)
                    category = Category.objects.get(slug=category_slug)
                show_size_slug = product_color["product"]["showSize"].lower()
                try:
                    show_size = Size.objects.get(slug=show_size_slug)
                except:
                    Size.objects.create(
                        slug=show_size_slug, name=show_size_slug.upper()
                    )
                    show_size = Size.objects.get(slug=show_size_slug)
                try:
                    Product.objects.create(
                        id=id,
                        name=name,
                        parent=product_obj,
                        description=description,
                        category=category,
                        discounted_price=discounted_price * coefficient,
                        selling_price=selling_price * coefficient,
                        original_price=original_price * coefficient,
                        brand=brand,
                        campaign=campaign,
                        currency=currency,
                        color=color,
                        show_size=show_size,
                    )
                except IntegrityError:
                    pass

                product_obj = Product.objects.get(pk=id)
                images_list2 = product_color["product"]["images"]

                for image_url in images_list:
                    Image.objects.get_or_create(product=product_obj, image=image_url)


# class UpdateProduct:
#     def __init__(self):
#         pass

#     def update_product_from_id(self, id):
#         scraper = TrendyolScraper()
#         try:
#             Product.objects.get(pk=id).delete()
#         except:
#             pass
#         try:
#             product = scraper.get_product_from_id(id)
#         except:
#             return False
#         id = product["id"]
#         name = product["name"]
#         link = product["link"]
#         campaign = product["campaign"]
#         discounted_price = product["price"]["discountedPrice"]["value"]
#         selling_price = product["price"]["sellingPrice"]["value"]
#         original_price = product["price"]["originalPrice"]["value"]
#         currency = product["price"]["currency"]
#         description = product["description"]
#         brand_slug = product["brand"]["slug"]
#         try:
#             brand = Brand.objects.get(slug=brand_slug)
#         except:
#             Brand.objects.create(slug=brand_slug, brand=brand_slug)
#             brand = Brand.objects.get(slug=brand_slug)
#         color_slug = product["showColor"]
#         try:
#             color = Color.objects.get(slug=color_slug)
#         except:
#             Color.objects.create(slug=color_slug, color=color_slug)
#             color = Color.objects.get(slug=color_slug)
#         category_slug = product["category"]["slug"]
#         try:
#             category = Category.objects.get(slug=category_slug)
#         except:
#             Category.objects.create(slug=category_slug, title=category_slug)
#             category = Category.objects.get(slug=category_slug)
#         show_size_slug = product["showSize"].lower()
#         try:
#             show_size = SizeL.objects.get(slug=show_size_slug)
#         except:
#             SizeL.objects.create(slug=show_size_slug, name=show_size_slug.upper())
#             show_size = SizeL.objects.get(slug=show_size_slug)
#         Product.objects.create(
#             id=id,
#             name=name,
#             link=link,
#             description=description,
#             category=category,
#             discounted_price=discounted_price,
#             selling_price=selling_price,
#             original_price=original_price,
#             brand=brand,
#             campaign=campaign,
#             currency=currency,
#             color=color,
#             show_size=show_size,
#         )

#         all_sizes = product["sizes"]
#         product_obj = Product.objects.get(pk=id)
#         images_list = product["images"]
#         for image_url in images_list:
#             Image.objects.get_or_create(product=product_obj, image=image_url)
#             print("success!")
#         # reviews = product["reviews"]
#         # Rating.objects.filter(product=product_obj).delete()
#         # for review in reviews:
#         #     author = review["user"]
#         #     rate = review["rate"]
#         #     comment = review["comment"]
#         #     date = review["date"]
#         #     Rating.objects.create(product=product_obj,author=author, rating=rate, created_at=date, comment=comment)
#         for size in all_sizes:
#             value_slug = size["value"].lower()
#             try:
#                 value = SizeL.objects.get(slug=value_slug)
#             except:
#                 SizeL.objects.create(slug=value_slug, name=value.upper())
#                 value = SizeL.objects.get(slug=value_slug)
#             in_stock = size["inStock"]
#             price = size["price"]
#             currency = size["currency"]
#             AllSizes.objects.create(
#                 product=product_obj,
#                 value=value,
#                 in_stock=in_stock,
#                 price=price,
#                 currency=currency,
#             )
#         return True


# # p = UpdateProduct()
# # p.update_product_from_id(73352731)
