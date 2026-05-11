# Author

Prepared for: Sammy Ford

---
# Structural Improvement Plan

## Original Prompt

> “Now create a Structural Improvement Plan. This plan should focus on improving organization, layering, maintainability, and seperation of concerns. This plan should refactor the code using functions, methods, classes, and object-oriented design. It must have all these features, login, registration, logout, session state, sidebar, role-based routing, Use of multi page design, at least two distinct user roles, CRUD functionality, JSON data Storage, user-sepcific or role-specific dashboards, clear navigation, usable design, test accounts shown on log in page, visible sample records for each role. This is just a plan, dont make any changes yet. Record the original prompt at the top of the file you create and label it Original Prompt, all prompts asked afterward should be stored on the file under the Original Prompt at the top of the page.”

### Additional Prompts

> “right now focus only on structural improvements, remove any UI Improvements.”

> “please save the prompts in the file under original prompt.”

---

# Plan Objective

The purpose of this refactor is to transform the current single-file Streamlit application into a modular, maintainable, and scalable application with clear architectural separation between:

* UI
* business logic
* data management
* models
* utilities
* routing

The plan focuses on improving:

* organization
* readability
* reusability
* maintainability
* scalability
* separation of concerns
* user experience

No implementation changes are included in this document.

---

# Current Structural Problems

## Single File Architecture

All functionality currently exists inside one Python file, including:

* UI rendering
* authentication
* inventory management
* sales logic
* chatbot logic
* JSON persistence
* session management

This creates:

* duplicated code
* tight coupling
* poor scalability
* difficult debugging
* limited reusability

---

## Mixed Responsibilities

UI components directly:

* modify data
* validate input
* process orders
* calculate metrics
* handle persistence

This prevents clear separation between presentation and business logic.

---

## Lack of Reusable Structures

The current application does not use:

* reusable functions
* service classes
* data models
* shared utilities
* reusable UI components

---

# Refactor Goals

The refactor should preserve all existing functionality while restructuring the application into a layered architecture.

Required functionality to preserve:

* login
* registration
* logout
* session state
* sidebar navigation
* role-based routing
* multi-page structure
* CRUD operations
* JSON persistence
* owner and employee roles
* dashboards
* chatbot assistant
* analytics displays
* inventory workflows

Additional required structural features:

* test accounts visible on login page
* visible sample records
* clear navigation

---

# Proposed Application Architecture

# 1. UI Layer

## Purpose

Responsible only for:

* rendering pages
* displaying data
* collecting user input
* navigation
* user feedback

The UI layer should not directly contain business logic.

---

## Proposed Multi-Page Structure

### Main Application

* `app.py`
* session initialization
* sidebar rendering
* routing entry point

### Pages Directory

#### Public Pages

* Home Page
* Login Page
* Registration Page

#### Owner Pages

* Owner Dashboard
* Inventory Management
* Sales Analytics
* Reports Page

#### Employee Pages

* Employee Dashboard
* Sales Entry
* Catalog Viewer
* Low Stock Viewer

---

---

# 2. Service Layer

## Purpose

Handles all business logic separately from the UI.

---

## Proposed Services

### Authentication Service

Responsibilities:

* login validation
* registration
* logout
* role verification
* session updates

### Inventory Service

Responsibilities:

* create products
* update inventory
* restock products
* discontinue products
* low stock checks

### Order Service

Responsibilities:

* create orders
* update inventory after sales
* calculate totals
* manage order history

### Analytics Service

Responsibilities:

* sales metrics
* inventory metrics
* revenue calculations
* most popular item calculations

### Chatbot Service

Responsibilities:

* chatbot responses
* predefined business questions
* reusable chat logic

---

# 3. Data Layer

## Purpose

Centralize all JSON read/write operations.

The UI and services should never directly open files.

---

## Proposed Data Structure

### Repositories

* User Repository
* Inventory Repository
* Order Repository
* Discontinued Repository

Responsibilities:

* JSON loading
* JSON saving
* validation
* file handling
* data retrieval

---

## JSON Storage Requirements

The refactor must preserve JSON-based persistence.

Required files:

* users.json
* inventory.json
* orders.json
* discontinued_items.json

---

# 4. Models Layer

## Purpose

Replace loose dictionaries with structured classes.

---

## Proposed Classes

### User Class

Fields:

* id
* email
* full_name
* password
* role

Methods:

* validate_login()
* to_dict()
* from_dict()

---

### InventoryItem Class

Fields:

* id
* name
* price
* stock

Methods:

* restock()
* reduce_stock()
* is_low_stock()
* to_dict()

---

### Order Class

Fields:

* order_id
* customer
* item
* quantity
* total
* status

Methods:

* calculate_total()
* to_dict()

---

# 5. Utilities Layer

## Purpose

Store reusable helper functionality.

---

## Proposed Utilities

### Session Utilities

* initialize session state
* clear session state
* route protection

### Validation Utilities

* validate email
* validate password
* validate numeric input

### Formatting Utilities

* currency formatting
* status formatting
* reusable UI labels

---

# Session State Plan

## Required Session Variables

* current page
* logged in status
* active user
* role
* chatbot messages

---

## Session Responsibilities

Session state should control:

* routing
* authentication
* dashboard access
* user-specific content
* chat persistence

---

# Role-Based Routing Plan

## Owner Role Access

Owner users should access:

* analytics
* inventory management
* reporting tools
* product CRUD operations
* order visibility

---

## Employee Role Access

Employee users should access:

* sales entry
* catalog viewing
* low stock viewing
* limited inventory interaction

---

## Route Protection

Unauthorized users should not access restricted pages.

All pages should validate:

* login state
* user role
* session integrity

---

# CRUD Functionality Plan

## Inventory CRUD

Required operations:

* Create products
* Read inventory
* Update price/stock
* Delete/discontinue products

---

## User CRUD

Required operations:

* Create accounts
* Read user data
* Update profiles
* Delete/deactivate accounts

---

## Order CRUD

Required operations:

* Create orders
* Read order history
* Update order status
* Delete/cancel orders

---

# Dashboard Plan

## Owner Dashboard

Should include:

* inventory metrics
* sales metrics
* low stock alerts
* recent orders
* chatbot assistant
* quick management actions

---

## Employee Dashboard

Should include:

* catalog access
* sales entry
* low stock alerts
* recent activity
* chatbot assistant

---

# Navigation Plan

## Sidebar Requirements

Sidebar should include:

* role-specific navigation
* logout button
* current user display
* dashboard shortcuts

---

## Navigation Structure

* centralized navigation logic
* consistent page naming
* scalable page organization

---

# Visible Demo/Test Data Plan

## Login Page

The login page should visibly display:

* Owner test account
* Employee test account
* role descriptions

---

## Sample Data Visibility

Each dashboard should display:

* visible inventory samples
* sample orders
* sample analytics

This ensures the application remains demonstrable even before live data is added.

---

# Maintainability Improvements

## Goals

The new structure should improve:

* code readability
* debugging
* feature expansion
* testing
* scalability
* onboarding for future developers

---

## Expected Refactor Benefits

* reduced duplication
* reusable logic
* easier maintenance
* cleaner UI organization
* safer data handling
* simpler future feature additions
* clearer separation of responsibilities

---

# Final Assessment

The current application already contains the core workflows needed for a bakery management system, but the structure is tightly coupled and difficult to scale.

This refactor plan focuses on preserving all existing functionality while reorganizing the application into a layered, object-oriented architecture using:

* functions
* methods
* reusable services
* models/classes
* repositories
* utilities
* multi-page Streamlit design

The goal is to create a cleaner, more maintainable, and extensible application without changing the core user workflows.
