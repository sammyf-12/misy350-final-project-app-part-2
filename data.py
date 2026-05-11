
import json
from pathlib import Path


class DataManager:

    USERS_FILE = Path("users.json")
    INVENTORY_FILE = Path("inventory.json")
    ORDERS_FILE = Path("orders.json")
    DISCONTINUED_FILE = Path("discontinued_items.json")

    @staticmethod
    def load_json_data(file_path):

        if file_path.exists():

            with open(file_path, "r") as file:
                return json.load(file)

        return []

    @staticmethod
    def save_json_data(file_path, data):

        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    @classmethod
    def load_users(cls):
        return cls.load_json_data(cls.USERS_FILE)

    @classmethod
    def save_users(cls, users):
        cls.save_json_data(cls.USERS_FILE, users)

    @classmethod
    def load_inventory(cls):
        return cls.load_json_data(cls.INVENTORY_FILE)

    @classmethod
    def save_inventory(cls, inventory):
        cls.save_json_data(cls.INVENTORY_FILE, inventory)

    @classmethod
    def load_orders(cls):
        return cls.load_json_data(cls.ORDERS_FILE)

    @classmethod
    def save_orders(cls, orders):
        cls.save_json_data(cls.ORDERS_FILE, orders)

    @classmethod
    def load_discontinued_items(cls):
        return cls.load_json_data(cls.DISCONTINUED_FILE)

    @classmethod
    def save_discontinued_items(cls, items):
        cls.save_json_data(cls.DISCONTINUED_FILE, items)
