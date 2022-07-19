import ujson
import asyncio
from time import time

from .trendyol_service import TrendyolService

class FolderAndFileUtils:
    @staticmethod
    def path_exist(name : str):
        from os import path

        return path.exists(name)

    @staticmethod
    def create_file(path_and_name: str, data: str):
        path_list = path_and_name.split("/")[:-1]

        paths = ""
        for path in path_list:
            paths += f"{path}/"
            FolderAndFileUtils.create_folder(paths)

        with open(path_and_name, "w", encoding="utf-8") as f:
            f.write(data)

    @staticmethod
    def create_folder(name):
        from os import mkdir

        if FolderAndFileUtils.path_exist(name):
            return
        mkdir(name)


class DictionaryUtils:
    @staticmethod
    def get_recursively(search_dict: dict(), to_find):
        fields_found = []

        for key, value in search_dict.items():
            if key == to_find:
                fields_found.append(value)

            elif isinstance(value, dict):
                results = DictionaryUtils.get_recursively(value, to_find)
                for result in results:
                    fields_found.append(result)

            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        more_results = DictionaryUtils.get_recursively(item, to_find)
                        for another_result in more_results:
                            fields_found.append(another_result)

        return fields_found

    @staticmethod
    def get_dict_by_key_value(lst: list, key, value):
        for item in lst:  # TODO: Speed up search
            if item[key] == value:
                my_item = item
                break
        else:
            # raise Exception(f"dict with '{key}: {value}' wasnt founded")
            return None

    # Not stable
    # @staticmethod
    # def get_dict_by_key_value(lst: list, key, value):
    #     next(
    #       item for item in lst if item[key] == value
    #     )

    @staticmethod
    def get_unique_list(lst: list):
        return [dict(t) for t in {tuple(d.items()) for d in lst}]

    @staticmethod
    def generate_tree(data: list, parent, parent_key):
        levels = {}

        for n in data:
            levels.setdefault(n.get(parent, None), []).append(n)

        def build_tree(parent_id=None):
            nodes = [dict(n) for n in levels.get(parent_id, [])]
            for n in nodes:
                children = build_tree(n[parent_key])
                if children:
                    n["children"] = children
            return nodes

        return build_tree()

    # Not stable
    #  @staticmethod
    # def generate_tree(data, parent, parent_key):
    # new_data = data.copy()

    # for i in range(len(new_data) - 1, -1, -1):
    #     data[i]["children"] = [
    #         child for child in new_data if child[parent] == new_data[i][parent_key]
    #     ]

    #     for child in new_data[i]["children"]:
    #         new_data.remove(child)

    # return new_data


class TrendyolScraper(TrendyolService):
    # TODO: Finish
    def get_product_from_id(self, id):
        pass

    def get_all_product_cards(self, write2file=False):
        print("\nSearching for categories.json")

        if not FolderAndFileUtils.path_exist("output/categories.json"):
            print("Starting parsing categories")

            self.get_all_categories(write2file=True)

            print("\nFinished parsing categories")
            print("\nCategories saved to categories.json")
        else:
            print("categories.json found")

        print("\nStarting parsing products")
        print("Processed: ")

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.fetch_all_product_cards())
        loop.close()

        if write2file:
            FolderAndFileUtils.create_file(
                "output/products.json", ujson.dumps(self.all_products)
            )

        print("\nFinished parsing products")

        return self.all_products

    def get_all_colors(self, write2file=False):
        asyncio.run(self.fetch_all_colors())

        if write2file:
            FolderAndFileUtils.create_file(
                "output/colors.json", ujson.dumps(self.all_colors)
            )

        return DictionaryUtils.get_unique_list(self.all_colors)

    def get_all_sizes(self, write2file=False):
        asyncio.run(self.fetch_all_sizes())

        if write2file:
            FolderAndFileUtils.create_file(
                "output/sizes.json", ujson.dumps(self.all_sizes)
            )

        return DictionaryUtils.get_unique_list(self.all_sizes)

    def get_all_brands(self, write2file=False):
        asyncio.run(self.fetch_all_brands())

        if write2file:
            FolderAndFileUtils.create_file(
                "output/brands.json", ujson.dumps(self.all_brands)
            )

        return DictionaryUtils.get_unique_list(self.all_brands)

    def get_all_categories(self, write2file=False):
        asyncio.run(self.fetch_all_categories())

        if write2file:
            FolderAndFileUtils.create_file(
                "output/categories.json", ujson.dumps(self.all_categories)
            )

        return self.all_categories


def main():
    scraper = TrendyolScraper()

    start_time = time()

    products = scraper.get_all_products()

    print(len(products))

    for product in products:
        if product["colors"]:
            FolderAndFileUtils.create_file("output/products/with_key.json", ujson.dumps(product))
            break

    print(time() - start_time)


if __name__ == "__main__":
    main()

# /erkek-hastane-cikisi-x-g2-c104159