# Original Prompt

Implement the ui plan.

# Additional Prompts

- For the next file, implement what changes to the UI I made naturally, for example changing where the AI chat box lays.
- Record any prompts I made to the original UI implementation.
- For each refinement, document what changed, why it changed, and which layer was affected.
- Record the original prompt at the top of the file you create and label it Original Prompt, all prompts asked afterward should be stored on the file under the Original Prompt at the top of the page.

# UI Implementation Refinement Log

## Purpose

This file documents the UI refinements made after implementing the UI improvement plan. Each refinement explains what changed, why it changed, and which layer was affected.

---

## Refinement 1: AI Chatbot Placement

### What Changed

The AI chatbot was moved from the bottom of the dashboard into a right-side column on both the Owner and Employee dashboards.

### Why It Changed

The chatbot felt disconnected when placed at the bottom of the page. Moving it to the side makes it easier to access while users are working in the dashboard.

### Layer Affected

UI Layer: `ui.py`

### Related Methods

- `render_owner_dashboard()`
- `render_employee_dashboard()`
- `render_chatbot()`

---

## Refinement 2: Chatbot Loading Spinner

### What Changed

A loading spinner was added while the AI generates a response.

### Why It Changed

Before the spinner, the response appeared suddenly, which made the chatbot feel less interactive. The spinner gives users feedback that the app is processing their question.

### Layer Affected

UI Layer: `ui.py`

### Related Method

- `render_chatbot()`

---

## Refinement 3: Chat History Reset on Logout

### What Changed

Chat history now resets when a user logs out.

### Why It Changed

This prevents one user from seeing another user’s previous chatbot conversation. It also keeps Owner and Employee sessions separate.

### Layer Affected

UI Layer: `ui.py`

### Related Methods

- `render_sidebar()`
- `reset_chat()`

---

## Refinement 4: Inventory Card Display

### What Changed

Inventory records were changed from raw dictionary output into readable product cards.

Each card now displays:

- Product name
- Price
- Stock
- Stock status

### Why It Changed

Raw dictionary output was hard to read and did not look like a finished dashboard. Product cards make the app cleaner and easier to understand.

### Layer Affected

UI Layer: `ui.py`

### Related Method

- `render_inventory_card()`

---

## Refinement 5: Consistent Stock Status Labels

### What Changed

Inventory items now show consistent status labels:

- `Low` for stock less than or equal to 5
- `In Stock` for stock above 5

### Why It Changed

The Owner and Employee dashboards needed consistent inventory formatting. This makes both dashboards look more professional and easier to compare.

### Layer Affected

UI Layer: `ui.py`

### Related Method

- `render_inventory_card()`

---

## Refinement 6: Improved Sidebar Navigation

### What Changed

The sidebar now changes based on whether the user is logged in and which role they have.

### Why It Changed

Users should only see navigation options that apply to them. This supports clearer navigation and role-based routing.

### Layer Affected

UI Layer: `ui.py`

### Related Method

- `render_sidebar()`

---

## Refinement 7: Login Page Test Accounts

### What Changed

The login page includes demo/test accounts inside an expander.

### Why It Changed

The project requires test accounts to be visible on the login page. This also makes the app easier to test during grading or demonstration.

### Layer Affected

UI Layer: `ui.py`

### Related Method

- `render_login_page()`

---

## Refinement 8: Registration Validation

### What Changed

The registration page checks for missing fields and duplicate emails.

### Why It Changed

This prevents incomplete accounts and avoids creating multiple users with the same email.

### Layers Affected

UI Layer: `ui.py`  
Service Layer: `services.py`

### Related Methods

- `render_registration_page()`
- `AuthService.find_user_by_email()`
- `AuthService.register_user()`

---

## Refinement 9: Login Validation Feedback

### What Changed

The login page gives clearer feedback for missing inputs and invalid credentials.

### Why It Changed

Users need to understand why login did not work instead of only seeing a generic failure.

### Layers Affected

UI Layer: `ui.py`  
Service Layer: `services.py`

### Related Methods

- `render_login_page()`
- `AuthService.login()`

---

## Refinement 10: Order Card Display

### What Changed

Order records are displayed as readable cards instead of raw dictionary output.

Each order card shows:

- Order ID
- Item
- Quantity
- Total
- Status

### Why It Changed

This makes order history easier for the Owner to read and keeps the dashboard style consistent.

### Layer Affected

UI Layer: `ui.py`

### Related Method

- `render_order_card()`

---

## Refinement 11: Clearer Feedback Messages

### What Changed

Feedback messages were improved for common user actions.

Examples include:

- Product added
- Product updated
- Product deleted
- Sale logged
- Insufficient stock
- No orders yet
- No low stock items

### Why It Changed

Users need confirmation after actions. Clear feedback makes the app easier to use and easier to demo.

### Layers Affected

UI Layer: `ui.py`  
Service Layer: `services.py`

### Related Methods

- `render_owner_dashboard()`
- `render_employee_dashboard()`
- `InventoryService`
- `OrderService`

---

## Refinement 12: Role-Based Dashboard Layouts

### What Changed

The Owner and Employee dashboards were made more consistent while still showing role-specific content.

### Why It Changed

Both dashboards should feel like part of the same website, but each role should still only see tools relevant to their job.

### Layer Affected

UI Layer: `ui.py`

### Related Methods

- `render_owner_dashboard()`
- `render_employee_dashboard()`

---

## Refinement 13: Chatbot UI Kept Separate From AI Logic

### What Changed

The UI displays the chatbot, but the OpenAI prompt and response generation stay in the service layer.

### Why It Changed

This keeps the UI layer focused on layout and user interaction while keeping AI logic separate.

### Layers Affected

UI Layer: `ui.py`  
Service Layer: `services.py`

### Related Methods

- `render_chatbot()`
- `AIChatAssistant.get_ai_response()`
- `AIChatAssistant.build_prompt()`

---

## Summary

The refinements improved the website’s usability without changing the core purpose of the app.

The biggest UI improvements were:

- moving the chatbot to the side column
- adding a spinner while the chatbot responds
- resetting chat on logout
- replacing raw data output with readable cards
- improving role-based navigation
- adding clearer feedback messages
- keeping Owner and Employee dashboards consistent

Most refinements affected the UI layer, while validation and chatbot behavior also connected to the service layer.
