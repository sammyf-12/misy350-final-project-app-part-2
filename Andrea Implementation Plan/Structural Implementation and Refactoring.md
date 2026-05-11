# Original Prompt

Now that we implemented the structural changes, review which files and layers changed. If any change affects another layer explain why. Record the original prompt at the top of the file you create and label it Original Prompt, all prompts asked afterward should be stored on the file under the Original Prompt at the top of the page.

# Additional Prompts

- None.

# Implementation and Structural Refactoring Review

## Overview

The application was refactored from one large Streamlit file into a layered, object-oriented structure. The updated structure improves organization, maintainability, and separation of concerns while preserving the main Sunshine Bakery website features.

The refactor separates the project into these main files:

- `app.py`
- `ui.py`
- `services.py`
- `data.py`
- `models.py`
- JSON data files

Each file now has a clearer responsibility.

---

## 1. `app.py` — App Runner Layer

### Purpose

`app.py` is now the main starting point of the application. It should stay small and should not contain dashboard logic, data logic, or business rules.

### What Changed

This file now handles:

- Streamlit page configuration
- Background styling
- Session state initialization
- Creating service objects
- Creating the UI manager object
- Running the application

### Why This Matters

The original app mixed setup, UI, data handling, and business logic in one file. Moving the startup logic into `app.py` makes the application easier to run and explain.

### Layer Impact

`app.py` connects the layers together. It creates the service objects and passes them into the UI layer.

Because of this, if a new service is added later, `app.py` may need to be updated so the UI can access it.

---

## 2. `ui.py` — UI Layer

### Purpose

`ui.py` controls what the user sees and interacts with. This includes pages, forms, buttons, dashboards, containers, tabs, metrics, and the chatbot display.

### What Changed

The Streamlit interface was moved into a `UIManager` class.

### Main Methods

- `render_sidebar()`
- `render_login_page()`
- `render_registration_page()`
- `render_owner_dashboard()`
- `render_employee_dashboard()`
- `render_chatbot()`
- `render_inventory_card()`
- `render_order_card()`
- `render_application()`

### UI Responsibilities

The UI layer now handles:

- Login screen
- Registration screen
- Sidebar navigation
- Logout button
- Owner dashboard
- Employee dashboard
- Role-based page display
- Inventory display cards
- Sales/order display cards
- Chatbot layout and input
- Loading spinner while the chatbot responds

### Dashboard Layout

The owner and employee dashboards now use a clearer two-column layout:

- Main dashboard content on the left
- AI chatbot on the right

This makes the chatbot easier to access without placing it at the bottom of the page.

### Inventory Display

Inventory records are now shown as readable product cards instead of raw dictionary-style data. Each card shows:

- Product name
- Price
- Stock
- Status label such as `Low` or `In Stock`

This improves usability and makes the owner and employee dashboards more consistent.

### Chatbot Display

The chatbot is now part of the UI layer only for display purposes. The UI handles:

- Showing example questions
- Showing the chat history
- Displaying the user message
- Showing a loading spinner
- Displaying the assistant response
- Keeping the chatbot in the side column

The actual OpenAI response logic is handled in the service layer.

### Logout Behavior

When a user logs out, chat history is reset. This prevents an employee from seeing a previous owner’s chatbot conversation, or the opposite.

### Layer Impact

The UI layer depends on the service layer.

For example:

- Login form calls `AuthService`
- Registration form calls `AuthService`
- Inventory forms call `InventoryService`
- Sales form calls `OrderService`
- Chatbot input calls `AIChatAssistant`

If a UI form changes its input fields, the related service method may also need to change.

---

## 3. `services.py` — Service Layer

### Purpose

`services.py` contains the business logic for the application. This keeps the UI cleaner and prevents Streamlit code from being mixed with calculations and application rules.

### Classes Included

- `AuthService`
- `InventoryService`
- `OrderService`
- `AIChatAssistant`

---

## `AuthService`

### Responsibilities

`AuthService` handles:

- Finding users by email
- Validating login credentials
- Checking user role
- Registering new users

### Layer Impact

The login and registration pages in `ui.py` depend on this service. If the login rules change, the UI does not need to handle that logic directly.

---

## `InventoryService`

### Responsibilities

`InventoryService` handles:

- Loading inventory records
- Adding new products
- Updating product prices
- Restocking inventory
- Deleting/discontinuing products
- Calculating inventory metrics
- Identifying low stock items

### Layer Impact

The owner dashboard and employee dashboard depend on this service for inventory records and metrics.

If inventory field names change, this service and the UI display may both need updates.

---

## `OrderService`

### Responsibilities

`OrderService` handles:

- Logging sales
- Reducing inventory after a sale
- Saving orders
- Loading order records
- Calculating revenue
- Calculating units sold
- Calculating total sales

### Layer Impact

The employee dashboard uses this service when logging a sale. The owner dashboard uses it to show sales metrics and order records.

Because logging a sale affects both orders and inventory, this service impacts multiple data files.

---

## `AIChatAssistant`

### Responsibilities

`AIChatAssistant` handles:

- Loading the OpenAI API key
- Creating the OpenAI client
- Building the system prompt
- Passing chat history to OpenAI
- Returning the AI response

### Chatbot Prompt Structure

The chatbot prompt is designed to keep responses focused on the bakery system. It includes:

- Inventory data
- Order data
- Discontinued item data
- Low stock definition
- Instructions to answer clearly and concisely

This prevents the assistant from acting like a generic chatbot and helps it answer questions based on the website’s data.

### Layer Impact

The chatbot affects both the UI and service layers:

- `ui.py` displays the chatbot and collects the user’s question
- `services.py` sends the question and data context to OpenAI
- `data.py` provides the inventory, order, and discontinued item data used in the prompt

If the chatbot needs more data later, the service layer should be updated to load that data from `DataManager`.

---

## 4. `data.py` — Data Layer

### Purpose

`data.py` centralizes all JSON data loading and saving.

### Main Class

`DataManager`

### Responsibilities

`DataManager` handles:

- Loading users
- Saving users
- Loading inventory
- Saving inventory
- Loading orders
- Saving orders
- Loading discontinued items
- Saving discontinued items
- Creating default JSON files if needed

### JSON Files Used

- `users.json`
- `inventory.json`
- `orders.json`
- `discontinued_items.json`

### Why This Matters

Before the refactor, JSON logic was repeated throughout the app. Now, data access is centralized, which makes the code easier to maintain and reduces duplicate file-handling logic.

### Layer Impact

The service layer depends on the data layer.

The UI should not directly open or save JSON files. Instead, the UI calls service methods, and the services use `DataManager`.

If the structure of a JSON file changes, the data layer and service layer may need updates.

---

## 5. `models.py` — Models / Classes Layer

### Purpose

`models.py` stores the main object models for the application.

### Classes Included

- `User`
- `InventoryItem`
- `Order`

### `User`

Represents a website user.

Fields include:

- user ID
- full name
- email
- password
- role

The user model also includes role-based access logic.

### `InventoryItem`

Represents a product in inventory.

Fields include:

- item ID
- name
- price
- stock

Methods include:

- restock
- reduce stock
- check low stock

### `Order`

Represents a sale/order.

Fields include:

- order ID
- customer
- item
- quantity
- total
- status

### Layer Impact

The current app still mainly uses dictionaries from JSON files, but the models support the object-oriented design requirement and provide a clearer structure for future improvements.

---

## Cross-Layer Changes

## UI Layer to Service Layer

The UI no longer performs most business logic directly. Instead, it collects input and calls service methods.

Examples:

- Login button calls `AuthService.login()`
- Register button calls `AuthService.register_user()`
- Add Product form calls `InventoryService.create_new_record()`
- Update Product form calls `InventoryService.update_record_status()`
- Delete Product button calls `InventoryService.delete_product()`
- Log Sale form calls `OrderService.create_new_record()`
- Chat input calls `AIChatAssistant.get_ai_response()`

### Why This Matters

This improves separation of concerns. The UI focuses on display, while the service layer handles decisions and calculations.

---

## Service Layer to Data Layer

The service layer depends on the data layer for persistence.

Examples:

- `InventoryService` loads and saves inventory
- `OrderService` loads and saves orders
- `AuthService` loads and saves users
- `AIChatAssistant` loads inventory, orders, and discontinued items for context

### Why This Matters

Changing how data is stored should mainly affect `data.py`, not every UI page.

---

## Data Layer to UI and Chatbot

The JSON files provide the data shown in the dashboards and used by the chatbot.

Examples:

- Inventory cards use inventory JSON records
- Sales metrics use order JSON records
- Login uses user JSON records
- Chatbot prompt uses inventory, order, and discontinued item JSON records

### Why This Matters

Field names must stay consistent. Changing fields such as `name`, `price`, `stock`, `quantity`, `total`, or `role` could break multiple layers.

---

## Important Dependencies

### Streamlit

Used in the UI layer for:

- pages
- forms
- buttons
- columns
- tabs
- containers
- metrics
- chat input
- chat messages
- session state

### JSON and Pathlib

Used in the data layer for:

- reading JSON files
- writing JSON files
- creating default data files

### Dotenv and OpenAI

Used in the service layer for:

- loading the API key
- connecting to OpenAI
- generating chatbot responses

---

## What Should Be Protected After Refactoring

### Protect `app.py`

Do not add dashboard content, forms, calculations, or JSON logic here.

### Protect `ui.py`

Keep Streamlit display code here. Do not add direct JSON reads/writes.

### Protect `services.py`

Keep business logic here. Do not add Streamlit UI code.

### Protect `data.py`

Keep file loading and saving here. Do not add dashboard logic.

### Protect `models.py`

Keep models simple. Do not add Streamlit or JSON file operations.

### Protect Session State

Important keys include:

- `logged_in`
- `user`
- `page`
- `messages`

Breaking these can affect login, routing, logout, and chatbot history.

### Protect JSON Field Names

Important fields include:

- `email`
- `password`
- `role`
- `full_name`
- `name`
- `price`
- `stock`
- `quantity`
- `total`
- `status`

### Protect Chatbot Flow

The chatbot should continue to:

- appear in the dashboard side column
- show example questions
- show a spinner while responding
- reset chat history on logout
- use inventory, order, and discontinued item data
- keep prompt logic inside the service layer

---

## Final Summary

The structural refactor separates the Sunshine Bakery website into clearer layers:

- `app.py` starts and connects the application
- `ui.py` renders the Streamlit interface
- `services.py` handles business logic
- `data.py` handles JSON storage
- `models.py` contains object-oriented classes

The main benefit is that each part of the project now has a specific responsibility. This makes the app easier to test, explain, maintain, and improve without accidentally breaking unrelated parts of the system.
