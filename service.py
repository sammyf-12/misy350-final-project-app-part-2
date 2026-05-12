from data import DataManager
import os
from dotenv import load_dotenv
from openai import OpenAI

class User:

    def __init__(
        self,
        user_id,
        full_name,
        email,
        password,
        role
    ):
        self.user_id = user_id
        self.full_name = full_name
        self.email = email
        self.password = password
        self.role = role

    def can_access_page(self, page):

        owner_pages = ["owner_dashboard"]
        employee_pages = ["employee_dashboard"]

        if self.role == "Owner":
            return page in owner_pages

        if self.role == "Employee":
            return page in employee_pages

        return False


class InventoryItem:

    def __init__(self, item_id, name, price, stock, image=None):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.stock = stock
        self.image = image

    def restock(self, quantity):
        self.stock += quantity

    def reduce_stock(self, quantity):
        self.stock -= quantity

    def is_low_stock(self):
        return self.stock <= 5


class Order:

    def __init__(
        self,
        order_id,
        customer,
        item,
        quantity,
        total,
        status
    ):
        self.order_id = order_id
        self.customer = customer
        self.item = item
        self.quantity = quantity
        self.total = total
        self.status = status

    def update_status(self, new_status):
        self.status = new_status


class AuthService:

    def find_user_by_email(self, email):

        users = DataManager.load_users()

        for user in users:

            if user["email"] == email:
                return user

        return None

    def validate_login(self, email, password, role):

        user = self.find_user_by_email(email)

        if user:

            return (
                user["password"] == password
                and user["role"] == role
            )

        return False

    def login(self, email, password, role):

        if self.validate_login(email, password, role):
            return self.find_user_by_email(email)

        return None

    def register_user(self, user_data):

        users = DataManager.load_users()

        user_data["id"] = len(users) + 1

        users.append(user_data)

        DataManager.save_users(users)


class InventoryService:

    def get_inventory(self):
        return DataManager.load_inventory()

    def create_new_record(self, product):

        inventory = self.get_inventory()

        product["id"] = len(inventory) + 1

        inventory.append(product)

        DataManager.save_inventory(inventory)

    def update_record_status(
        self,
        item_name,
        new_price,
        restock_quantity
    ):

        inventory = self.get_inventory()

        for item in inventory:

            if item["name"] == item_name:
                item["price"] = new_price
                item["stock"] += restock_quantity

        DataManager.save_inventory(inventory)

    def delete_product(self, item_name):

        inventory = self.get_inventory()
        discontinued = (
            DataManager.load_discontinued_items()
        )

        updated_inventory = []

        for item in inventory:

            if item["name"] == item_name:
                discontinued.append(item_name)

            else:
                updated_inventory.append(item)

        DataManager.save_inventory(updated_inventory)
        DataManager.save_discontinued_items(discontinued)

    def calculate_inventory_metrics(self):

        inventory = self.get_inventory()

        return {
            "products": len(inventory),
            "stock": sum(
                item["stock"] for item in inventory
            ),
            "low_stock": sum(
                1 for item in inventory
                if item["stock"] <= 5
            ),
            "value": sum(
                item["price"] * item["stock"]
                for item in inventory
            )
        }


class OrderService:

    def create_new_record(
        self,
        item_name,
        quantity
    ):

        inventory = DataManager.load_inventory()
        orders = DataManager.load_orders()

        for item in inventory:

            if item["name"] == item_name:

                if item["stock"] >= quantity:

                    item["stock"] -= quantity

                    order = {
                        "order_id": len(orders) + 1,
                        "customer": "Walk-In Customer",
                        "item": item_name,
                        "quantity": quantity,
                        "total": item["price"] * quantity,
                        "status": "Completed"
                    }

                    orders.append(order)

                    DataManager.save_inventory(inventory)
                    DataManager.save_orders(orders)

                    return True

        return False

    def get_all_orders(self):
        return DataManager.load_orders()

    def filter_records_by_user(self, customer):

        orders = self.get_all_orders()

        return [
            order for order in orders
            if order["customer"] == customer
        ]

    def calculate_sales_metrics(self):

        orders = self.get_all_orders()

        return {
            "sales": len(orders),
            "units": sum(
                order["quantity"] for order in orders
            ),
            "revenue": sum(
                order["total"] for order in orders
            )
        }


class AIChatAssistant:
    load_dotenv()

    def __init__(self):
        self.api_key = os.getenv("OPEN_AI_KEY")

        if self.api_key:
            self.client = OpenAI(api_key=self.api_key)
        else:
            self.client = None

    def build_prompt(self):

        inventory = DataManager.load_inventory()
        orders = DataManager.load_orders()
        discontinued = (
            DataManager.load_discontinued_items()
        )

        return (
            "You are an AI assistant for The Sunshine Bakery and Shop website."
            "Help the owner and employees answer questions about orders, inventory, sales, menu items, and general bakery operations. Answer clearly and simply."
             "DO NOT say you cannot access the inventory system. "
            "Use the provided data to answer questions directly. "

            f"Inventory Data: {inventory}. "
            f"Order Data: {orders}. "
            f"Discontinued Items: {discontinued}. "

            "If the user asks for low stock items, identify products with stock less than or equal to 5."
        )
    
    def get_ai_response(self, chat_history):
        if self.client is None:
            return "OpenAI key was not found!"

        prompt_message = [
            {
                "role": "system",
                "content": self.build_prompt()
            }
        ]

        messages = prompt_message + chat_history

        response = self.client.chat.completions.create(
            model="gpt-5-mini",
            messages=messages
        )

        return response.choices[0].message.content