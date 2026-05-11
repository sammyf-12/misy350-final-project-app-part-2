# Original Prompt

Using what we just analyzed for both the structural and feature analysis of the current website, please create a structure improvement plan. This plan should focus on improving organization, layering, maintainability, and seperation of concerns. This is just a plan. Do not implement anything yet. This plan should refactor the code using functions, methods, classes, and object-oriented design. It must have all these features, login, registration, logout, session state, sidebar, role-based routing, Use of multi page design, at least two distinct user roles, CRUD functionality, JSON data Storage, user-sepcific or role-specific dashboards, clear navigation, usable design, test accounts shown on log in page, visible sample records for each role. Record the original prompt at the top of the file you create and label it Original Prompt, all prompts asked afterward should be stored on the file under the Original Prompt at the top of the page.

# Additional Prompts

- None yet.

# Sunshine Bakery Structure Improvement Plan

## Goal

Refactor the current Sunshine Bakery website into a cleaner object-oriented Streamlit application. The plan focuses on better organization, clearer layering, maintainability, and separation of concerns while keeping all required project features.

This is a planning document only. No code should be changed yet.

---

## Required Features To Preserve

The refactored website must keep:

- Login
- Registration
- Logout
- Session state
- Sidebar navigation
- Role-based routing
- Multi-page design
- At least two user roles: Owner and Employee
- CRUD functionality
- JSON data storage
- Role-specific dashboards
- Clear navigation
- Usable dashboard design
- Test accounts shown on login page
- Visible sample records for each role

---

## Proposed File Structure

The app should be split into separate files instead of keeping everything in one large Streamlit file.

```text
Final Project/
│
├── app.py
├── ui.py
├── services.py
├── data.py
├── models.py
│
├── users.json
├── inventory.json
├── orders.json
├── discontinued_items.json
│
└── .env
```

---

## Layer 1: App Runner

### File
`app.py`

### Purpose
This should be the smallest file. It should only start the app and connect the layers.

### Responsibilities
- Set Streamlit page configuration
- Initialize session state
- Create service objects
- Create the UI manager object
- Run the application

### Protect
Do not place dashboard logic, JSON logic, or business calculations here.

---

## Layer 2: UI Layer

### File
`ui.py`

### Main Class
`UIManager`

### Purpose
This layer controls what the user sees.

### Responsibilities
- Render sidebar
- Render login page
- Render registration page
- Render owner dashboard
- Render employee dashboard
- Render chatbot display
- Render forms, buttons, tabs, containers, and metrics
- Route users to the correct page based on role

### Important Methods
- `render_sidebar()`
- `render_login_page()`
- `render_registration_page()`
- `render_owner_dashboard()`
- `render_employee_dashboard()`
- `render_chatbot()`
- `render_application()`

### Protect
The UI layer should not directly read or write JSON files. It should call the service layer instead.

---

## Layer 3: Service Layer

### File
`services.py`

### Purpose
This layer handles application logic.

### Recommended Classes

#### `AuthService`
Handles:
- Login validation
- Registration
- Finding users
- Role checking

#### `InventoryService`
Handles:
- Viewing inventory
- Adding products
- Updating products
- Restocking products
- Deleting/discontinuing products
- Low stock calculations
- Inventory value calculations

#### `OrderService`
Handles:
- Logging sales
- Reducing stock after a sale
- Viewing orders
- Revenue calculations
- Units sold calculations
- Most popular item logic

#### `AIChatAssistant`
Handles:
- OpenAI setup
- Prompt building
- Chatbot responses
- Inventory/order/discontinued item context

### Protect
Keep business logic here. Do not put Streamlit UI code in the service layer.

---

## Layer 4: Data Layer

### File
`data.py`

### Main Class
`DataManager`

### Purpose
This layer handles JSON data storage.

### Responsibilities
- Load users
- Save users
- Load inventory
- Save inventory
- Load orders
- Save orders
- Load discontinued items
- Save discontinued items
- Create default JSON files if they do not exist

### Protect
The data layer should only handle data access. It should not calculate revenue, validate logins, or render UI.

---

## Layer 5: Models / Classes

### File
`models.py`

### Purpose
Models represent the main objects in the app.

### Recommended Classes

#### `User`
Fields:
- `user_id`
- `full_name`
- `email`
- `password`
- `role`

Methods:
- `can_access_page(page)`

#### `InventoryItem`
Fields:
- `item_id`
- `name`
- `price`
- `stock`

Methods:
- `restock(quantity)`
- `reduce_stock(quantity)`
- `is_low_stock()`

#### `Order`
Fields:
- `order_id`
- `customer`
- `item`
- `quantity`
- `total`
- `status`

Methods:
- `update_status(new_status)`

### Protect
Models should stay simple. They should not contain Streamlit code or JSON file operations.

---

## Session State Plan

Session state should be initialized once in `app.py`.

### Required Session Variables
- `logged_in`
- `user`
- `page`
- `messages`

### Optional Session Variables
- `owner_logged_in`
- `employee_logged_in`

### Recommended Improvement
Use one login flag instead of separate owner and employee flags.

Preferred:
```python
st.session_state["logged_in"]
st.session_state["user"]
st.session_state["page"]
```

Avoid relying on:
```python
st.session_state["owner_logged_in"]
st.session_state["employee_logged_in"]
```

because the user role can already be checked from `st.session_state["user"]["role"]`.

---

## Role-Based Routing Plan

The app should route users based on role.

### Owner
Can access:
- Owner dashboard
- Inventory management
- Add product
- Update product
- Delete/discontinue product
- Orders
- Chatbot

### Employee
Can access:
- Employee dashboard
- Catalog
- Sales logging
- Low stock view
- Chatbot

### Protect
Users should not be able to access another role’s dashboard by changing the page variable.

---

## Multi-Page Design Plan

The app should still behave like a multi-page website using session state routing.

### Pages
- Login page
- Registration page
- Owner dashboard
- Employee dashboard

### Navigation
The sidebar should show:
- Login/Register when logged out
- Dashboard button based on role when logged in
- Logout button when logged in

---

## CRUD Functionality Plan

### Inventory CRUD
Owner should be able to:
- Create products
- Read/view inventory
- Update product price and stock
- Delete/discontinue products

### Order CRUD / Workflow
Employee should be able to:
- Create sales/orders
- Read/view orders indirectly through dashboard data

### User CRUD / Registration
Users can:
- Create/register account
- Read login data through authentication flow

### Protect
Deleting products should continue to save discontinued items instead of losing the item completely.

---

## JSON Data Storage Plan

Keep the current JSON file storage because it matches the project scope.

### Files To Keep
- `users.json`
- `inventory.json`
- `orders.json`
- `discontinued_items.json`

### Improvement
Centralize all JSON loading/saving in `DataManager`.

### Protect
Do not scatter `json.load()` and `json.dump()` throughout the UI file.

---

## Dashboard Design Plan

### Owner Dashboard
Should show:
- Inventory metrics
- Sales metrics
- Inventory records
- Add product form
- Update product form
- Delete product form
- Orders
- Chatbot

### Employee Dashboard
Should show:
- Product catalog
- Sales form
- Low stock items
- Chatbot

### Sample Records
Each role should see sample records:
- Owner sees inventory and sales/order records
- Employee sees catalog and low stock records

---

## Chatbot Plan

The chatbot should be kept as a service class.

### UI Layer
Displays:
- Chat history
- Chat input
- Loading spinner
- Example questions

### Service Layer
Handles:
- OpenAI client
- Prompt
- Inventory/order context
- Response generation

### Protect
The chatbot should not write directly to JSON files unless specifically designed to do so later.

---

## Usability Improvement Plan

Recommended improvements:
- Use containers/cards for inventory records
- Use consistent “In Stock” and “Low” labels
- Keep chatbot in a side column
- Add loading spinner while AI responds
- Clear chat on logout
- Show test accounts on login page
- Keep sidebar navigation simple

---

## Refactor Implementation Order

### Step 1: Create Models
Move simple object definitions into `models.py`.

### Step 2: Create DataManager
Move all JSON load/save logic into `data.py`.

### Step 3: Create Services
Move login, inventory, order, and chatbot logic into `services.py`.

### Step 4: Create UIManager
Move all Streamlit rendering into `ui.py`.

### Step 5: Simplify app.py
Use `app.py` only to initialize and run the app.

### Step 6: Test Required Features
Test:
- login
- registration
- logout
- owner dashboard
- employee dashboard
- inventory CRUD
- sales logging
- JSON saving
- chatbot
- role-based access

---

## What Must Be Protected Before Refactoring

### Data
- Existing JSON files
- Inventory field names
- Order field names
- User field names

### Login Flow
- Test accounts
- Role-based access
- Session state routing

### Inventory Flow
- Stock updates
- Low stock calculation
- Discontinued items list

### Sales Flow
- Stock reduction after sales
- Order saving
- Revenue calculation

### Chatbot Flow
- OpenAI API key
- Chat history
- Prompt instructions
- Inventory/order context

---

## Final Summary

The improved structure should separate the app into clear layers:

- `app.py` starts the app
- `ui.py` displays the app
- `services.py` handles logic
- `data.py` handles JSON storage
- `models.py` defines objects

This keeps the required website features while making the project easier to maintain, explain, test, and expand.
