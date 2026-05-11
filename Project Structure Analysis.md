# Project Structure Analysis

## Original Prompt

> “I want you to review the current app structure of the website. The analysis should identify the UI Layer, Service Layer, data/database layer, models/classes, and important dependencies. This part is analysis only, but needs to be detailed for when the changes are implemented. Explain what should be protected before making changes. Record the original prompt at the top of the file you create and label it Original Prompt, all prompts asked afterward should be stored on the file under the Original Prompt at the top of the page.”

### Additional Prompts

> “please rename the file to Project Structure Analysis”

> “Please concise the file and remove redundancy”

> “Please store the other prompts I gave under original prompt”

---

# Files Reviewed

* `FinalProject(4).py`
* `inventory(4).json`
* `orders(4).json`
* `users(4).json`
* `discontinued_items(4).json`

---

# Application Overview

The project is a monolithic Streamlit application where the UI, business logic, session management, and JSON persistence are combined into a single Python file. The system currently supports:

* authentication
* inventory management
* sales logging
* analytics dashboards
* chatbot assistance
* JSON-based data storage

The application functions correctly but is tightly coupled and difficult to scale or maintain.

---

# 1. UI Layer

## Current Structure

The UI is built entirely with Streamlit inside `FinalProject(4).py`.

### Main UI Sections

* Home Page
* Registration Page
* Owner Login
* Owner Dashboard
* Employee Login
* Employee Dashboard

### Main UI Components

* `st.sidebar`
* `st.tabs`
* `st.columns`
* `st.container`
* `st.metric`
* `st.chat_input`
* `st.chat_message`

### Routing System

Navigation is controlled through:

```python
st.session_state["page"]
```

---

## UI Layer Issues

* All pages exist in one file
* Business logic is embedded directly inside UI blocks
* Chatbot logic is duplicated
* Inventory rendering logic repeats multiple times
* Deep nesting reduces maintainability

---

## UI Elements That Must Be Protected

### Session State

Critical variables:

```python
st.session_state["page"]
st.session_state["user"]
st.session_state["owner_logged_in"]
st.session_state["employee_logged_in"]
```

These control routing, authentication, and dashboard access.

### Streamlit Keys

Form keys and widget keys must remain unique to avoid UI conflicts.

### Navigation Workflow

Current workflow:

1. Login
2. Session update
3. Dashboard redirect
4. Data update
5. UI rerender

---

# 2. Service Layer

The application does not currently have a separated service layer. Business logic is directly mixed into the UI.

## Current Responsibilities

### Authentication Logic

* user login
* registration
* role verification

### Inventory Logic

* add product
* update price
* restock inventory
* delete/discontinue items
* low stock detection

### Order Logic

* sales logging
* order creation
* stock reduction
* revenue calculations

### Analytics Logic

* total sales
* units sold
* inventory value
* most popular item

### Chatbot Logic

The chatbot provides predefined responses using inventory and order data.

---

## Service Layer Issues

* No separation of concerns
* No reusable functions
* Repeated calculations
* Tight coupling between UI and data
* Minimal validation
* Passwords stored in plain text

---

## Logic That Must Be Protected

* inventory stock calculations
* order creation rules
* login verification
* role-based dashboard routing
* discontinued item tracking
* revenue calculations

---

# 3. Data / Database Layer

## Current Storage

The project uses JSON files as a lightweight database.

### Files

* `users.json`
* `inventory.json`
* `orders.json`
* `discontinued_items.json`

---

## Current Data Flow

### Read

```python
json.load()
```

### Write

```python
json.dump()
```

---

## Existing Data Structures

### User

```json
{
  "id": 1,
  "email": "...",
  "full_name": "...",
  "password": "...",
  "role": "Owner"
}
```

### Inventory Item

```json
{
  "id": 1,
  "name": "...",
  "price": 2.0,
  "stock": 20
}
```

### Order

```json
{
  "order_id": "...",
  "customer": "...",
  "item": "...",
  "quantity": 1,
  "total": 10.0,
  "status": "Placed"
}
```

---

## Data Layer Issues

* No database abstraction
* Direct file access throughout application
* No transaction protection
* No schema validation
* Orders store item names instead of IDs
* File overwrites may risk corruption

---

## Data Structures That Must Be Protected

* JSON file names
* existing key names
* inventory schema
* order schema
* ID generation logic
* stock update behavior

Changing field names would break dashboards, metrics, chatbot logic, and inventory workflows.

---

# 4. Models / Classes

## Current State

No formal classes or models exist.

The application uses dictionaries and lists for all data handling.

---

## Implicit Models

### User Model

Fields:

* id
* email
* full_name
* password
* role

### Inventory Model

Fields:

* id
* name
* price
* stock

### Order Model

Fields:

* order_id
* customer
* item
* quantity
* total
* status

---

## Model Issues

* No type safety
* No validation layer
* No encapsulation
* No reusable methods
* Any section can mutate data directly

---

# 5. Important Dependencies

## Core Dependencies

* Streamlit
* json
* pathlib.Path
* time
* datetime
* uuid

---

## Critical Dependency Risks

### Streamlit Session State

The entire application depends heavily on:

```python
st.session_state
```

Breaking session state behavior would affect:

* authentication
* routing
* dashboards
* chatbot history
* page rendering

---

# Critical Systems To Protect Before Refactoring

## Authentication

* login validation
* role permissions
* dashboard redirects

## Inventory System

* stock updates
* product creation
* product deletion
* discontinued tracking

## Order System

* order creation
* stock subtraction
* sales calculations

## JSON Persistence

* read/write behavior
* schema consistency
* file naming

## Session State

* routing
* login state
* chat history

---

# Final Assessment

The application is a functional prototype with clear workflows and good dashboard organization, but the architecture is tightly coupled and difficult to maintain at scale.

The most important areas to protect before implementing structural changes are:

* session state behavior
* JSON schema consistency
* authentication workflows
* inventory/order synchronization
* routing logic
* persistence behavior

Refactoring should be incremental and layer-based to avoid breaking application functionality.
