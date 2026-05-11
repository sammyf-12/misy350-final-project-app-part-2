# Original Prompt

We are now focusing on the ui improvement plan. This should be separate from the structural improvement plan. This plan should address missing features, improvements, UI design, Streamlit pages, routing, st.session_state, user actions, and feedback messages. This plan should refactor the code using functions, methods, classes, and object-oriented design. It must have all these features, login, registration, logout, session state, sidebar, role-based routing, Use of multi page design, at least two distinct user roles, CRUD functionality, JSON data Storage, user-specific or role-specific dashboards, clear navigation, usable design, test accounts shown on log in page, visible sample records for each role. Record the original prompt at the top of the file you create and label it Original Prompt, all prompts asked afterward should be stored on the file under the Original Prompt at the top of the page.

# Additional Prompts

- Please be more concise and remove any redundancy.

# Sunshine Bakery UI Improvement Plan

## Goal

Improve the Sunshine Bakery user interface and user experience while preserving the current object-oriented structure and required Streamlit functionality.

This is a UI planning document only. No implementation should occur yet.

---

## Required Features To Preserve

The improved UI must keep:

- Login
- Registration
- Logout
- Session state
- Sidebar navigation
- Role-based routing
- Multi-page design
- Two user roles: Owner and Employee
- CRUD functionality
- JSON data storage
- Role-specific dashboards
- Clear navigation
- Test accounts on login page
- Visible sample records

---

## Current UI Summary

The current app already includes:

- Login and registration pages
- Sidebar navigation
- Owner and Employee dashboards
- Inventory management
- Sales logging
- Order display
- Low stock display
- AI chatbot assistant
- JSON-backed records

The UI works well functionally but can be improved with:
- cleaner layouts
- clearer feedback messages
- more consistent dashboard design
- improved readability

---

## Streamlit Page Plan

The app should continue using page routing through:

```python
st.session_state["page"]
```

### Main Pages

- Login page
- Registration page
- Owner dashboard
- Employee dashboard

### UI Methods

Pages should remain separated into methods inside `UIManager`:

- `render_login_page()`
- `render_registration_page()`
- `render_owner_dashboard()`
- `render_employee_dashboard()`
- `render_sidebar()`
- `render_chatbot()`
- `render_application()`

---

## Sidebar Improvement Plan

### Logged Out

Show:
- Login
- Register

### Logged In

Show:
- User name
- User role
- Role-specific dashboard button
- Logout button

### Improvement

Only show pages the current role can access.

---

## Login Page Plan

### Features

The login page should include:

- Email field
- Password field
- Role selection
- Login button
- Demo accounts section

### Demo Accounts

- Owner: `owner@bakery.com / 123`
- Employee: `employee@bakery.com / 1234`

### Feedback

Use:
- `st.success()` for successful login
- `st.error()` for invalid credentials

---

## Registration Page Plan

### Features

The registration page should include:

- Full name
- Email
- Password
- Role selection
- Create Account button

### Improvements

Add:
- Required field validation
- Duplicate email validation

### Feedback

Use:
- `st.warning()` for missing fields
- `st.error()` for duplicate emails
- `st.success()` for successful registration

---

## Logout Plan

Logout should:
- clear the current user
- return to login
- reset chatbot history

This prevents role-specific chat history from carrying between users.

---

## Session State Plan

### Required Keys

- `logged_in`
- `user`
- `page`
- `messages`

### Improvement

Use:

```python
st.session_state["user"]["role"]
```

instead of separate owner/employee login flags.

---

## Role-Based Routing Plan

### Owner Access

Owner should access:
- Inventory management
- Orders
- Sales metrics
- AI chatbot

### Employee Access

Employee should access:
- Product catalog
- Sales form
- Low stock view
- AI chatbot

### Improvement

Check:
- login status
- user role

before rendering dashboards.

---

## Owner Dashboard Plan

### Sections

Owner dashboard should include:

- Inventory metrics
- Sales metrics
- Inventory records
- Add Product form
- Update Product form
- Delete Product form
- Orders
- AI chatbot

### Layout

Use:
- left column for dashboard content
- right column for chatbot

### Tabs

- Inventory
- Add Product
- Update Product
- Delete Product
- Orders

---

## Employee Dashboard Plan

### Sections

Employee dashboard should include:

- Product catalog
- Sales form
- Low stock list
- AI chatbot

### Layout

Use:
- left column for tasks
- right column for chatbot

### Tabs

- Catalog
- Sales
- Low Stock

---

## Inventory Display Plan

Replace raw dictionary output with inventory cards.

Each card should display:
- Product name
- Price
- Stock
- Status label

### Status Labels

- `Low` for stock <= 5
- `In Stock` otherwise

This keeps dashboards cleaner and more consistent.

---

## Orders Display Plan

Replace raw order dictionaries with order cards.

Each order card should show:
- Order ID
- Item
- Quantity
- Total
- Status

If no orders exist:

```python
st.info("No orders yet")
```

---

## CRUD UI Plan

### Create
Owner adds products.

### Read
Users view inventory and orders.

### Update
Owner updates price and stock.

### Delete
Owner discontinues products.

### Improvement

Each CRUD action should provide:
- clear labels
- validation
- success/error feedback
- rerun after updates

---

## Chatbot UI Plan

### Purpose

The chatbot helps users ask questions about:
- inventory
- revenue
- orders
- low stock
- discontinued items

### Placement

Keep the chatbot in the right-side dashboard column.

### Features

The chatbot should include:
- example questions
- message history
- loading spinner
- chat input

### Chat Reset

Reset messages on logout.

---

## Feedback Message Plan

### Login
- Success for valid login
- Error for invalid login

### Registration
- Warning for missing fields
- Error for duplicate email
- Success for account creation

### Inventory Actions
- Success for add/update/delete
- Warning for invalid input

### Sales
- Success for logged sale
- Error for insufficient stock

### Chatbot
- Spinner while loading response

---

## Missing UI Features To Consider Later

Possible future improvements:
- Inventory search
- Product filtering
- Sales charts
- Confirmation popups
- Receipt display
- Mobile responsiveness
- Better empty-state messages

---

## Object-Oriented UI Design

### Main Class

`UIManager`

### Helper Methods

Recommended reusable methods:
- `render_inventory_card()`
- `render_order_card()`
- `render_metric_row()`
- `render_chatbot()`

This reduces repeated Streamlit code.

---

## Implementation Order

1. Improve routing validation
2. Improve sidebar navigation
3. Improve login/registration validation
4. Improve dashboard layouts
5. Improve inventory and order displays
6. Improve CRUD feedback messages
7. Test role-specific workflows

---

## What To Protect

Protect:
- login flow
- role-based routing
- session state
- CRUD workflows
- JSON field names
- chatbot placement and behavior
- inventory/order displays
- chatbot reset on logout

---

## Final Summary

The UI improvement plan focuses on making the Sunshine Bakery website cleaner, more consistent, and easier to use while preserving:

- login
- registration
- logout
- CRUD functionality
- JSON storage
- role-based dashboards
- session state
- sidebar routing
- AI chatbot integration

The final UI should be easier to navigate, visually cleaner, and more maintainable within the existing object-oriented structure.
