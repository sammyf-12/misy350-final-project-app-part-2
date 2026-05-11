# Author

Prepared for: Sammy Ford

---
# UI Improvement Plan

## Original Prompt

> “Now create a document called UI Improvement Plan. This should be separate from the Structural Improvement Plan. This plan should address missing features, improvements, UI design, streamlit pages, routing, st.session_state, user action and feedback messages.his plan should refactor the code using functions, methods, classes, and object-oriented design. It must have all these features, login, registration, logout, session state, sidebar, role-based routing, Use of multi page design, at least two distinct user roles, CRUD functionality, JSON data Storage, user-sepcific or role-specific dashboards, clear navigation, usable design, test accounts shown on log in page, visible sample records for each role. Record the original prompt at the top of the file you create and label it Original Prompt, all prompts asked afterward should be stored on the file under the Original Prompt at the top of the page.”

### Additional Prompts

> “please make the document concise and remove redundancy.”

---

# Plan Objective

This plan focuses on improving the usability, navigation, workflow clarity, routing, session state handling, and overall user experience of the Sunshine Bakery application while preserving the current business workflows.

This is a planning document only and does not implement changes.

---

# Current UI Problems

## Navigation Issues

* Limited sidebar navigation
* Scattered routing logic
* Inconsistent dashboard flow
* Difficult scalability for additional pages

---

## Dashboard Issues

* Repeated layouts and duplicated UI sections
* Crowded dashboards with larger inventories
* Weak organization of metrics and workflows

---

## User Workflow Issues

* Minimal validation feedback
* No confirmation prompts for destructive actions
* Limited success/error messaging
* No workflow guidance or empty-state messaging

---

## Session State Issues

* Repetitive session logic
* Scattered login and routing conditions
* No centralized session utilities

---

# UI Refactor Goals

The redesign should preserve:

* login
* registration
* logout
* session state
* sidebar navigation
* role-based routing
* CRUD workflows
* JSON persistence
* owner and employee dashboards
* test accounts
* sample records

The redesign should improve:

* usability
* routing clarity
* dashboard organization
* user feedback
* reusable UI components
* scalable page structure

---

# Multi-Page Streamlit Plan

## Public Pages

* Home Page
* Login Page
* Registration Page

## Owner Pages

* Owner Dashboard
* Inventory Management
* Analytics Page
* Order History

## Employee Pages

* Employee Dashboard
* Sales Entry
* Catalog Viewer
* Low Stock Page

---

# Routing and Session State Plan

## Centralized Routing

Routing should use:

```python
st.session_state["page"]
```

Routing should:

* validate login state
* validate user roles
* redirect unauthorized users
* handle logout flow

---

## Required Session Variables

```python
st.session_state["page"]
st.session_state["logged_in"]
st.session_state["user"]
st.session_state["role"]
st.session_state["messages"]
```

---

## Session Improvements

Centralize:

* session initialization
* logout handling
* route protection
* role validation

---

# Sidebar Improvement Plan

The sidebar should include:

* current user display
* role display
* role-specific navigation
* dashboard shortcuts
* logout button

Goals:

* centralized navigation
* scalable page organization
* reduced clutter
* consistent user flow

---

# Login and Registration Plan

## Login Page

Should include:

* email field
* password field
* role selection
* visible test accounts
* login validation feedback
* registration navigation

---

## Registration Page

Should include:

* full name
* email
* password
* role selection
* validation feedback
* success confirmation

---

# Dashboard Improvement Plan

## Owner Dashboard

Should include:

* inventory metrics
* revenue metrics
* low stock alerts
* recent orders
* chatbot assistant
* inventory controls

Goals:

* grouped metrics
* reusable dashboard sections
* cleaner inventory management workflows

---

## Employee Dashboard

Should include:

* inventory viewer
* sales logging
* low stock viewer
* chatbot assistant
* sample records

Goals:

* simplified workflows
* cleaner inventory visibility
* role-focused actions

---

# CRUD Workflow Plan

## Inventory CRUD

Support:

* create products
* view inventory
* update inventory
* delete/discontinue products

UI improvements should include:

* validation feedback
* confirmation prompts
* inventory filtering/search
* success/error messaging

---

# User Feedback Plan

## Success Messages

Provide feedback for:

* login
* registration
* product creation
* inventory updates
* sales logging
* logout

---

## Warning/Error Messages

Provide feedback for:

* invalid credentials
* insufficient stock
* missing fields
* duplicate records
* unauthorized actions

---

## Empty-State Messages

Provide guidance when:

* inventory is empty
* no orders exist
* dashboards contain no data

---

# Reusable UI Structure Plan

The redesign should use reusable:

* dashboard cards
* inventory containers
* metrics sections
* forms
* alert messages
* navigation components

The UI should be refactored using:

* reusable functions
* methods
* classes
* object-oriented design

---

# JSON Data Visibility Plan

## Test Accounts

The login page should visibly display:

* Owner test account
* Employee test account

---

## Sample Records

Dashboards should visibly display:

* inventory examples
* sample orders
* analytics examples
* low stock examples

---

# Missing UI Features

## High Priority

* centralized routing
* reusable dashboard components
* validation feedback
* confirmation dialogs
* inventory search/filtering
* improved dashboard organization

## Medium Priority

* responsive layouts
* workflow indicators
* advanced filtering
* improved tables/cards

## Low Priority

* dark mode
* custom themes
* accessibility enhancements

---

# Final Assessment

The current UI is functional but repetitive and difficult to scale as additional workflows are added.

This plan focuses on improving:

* navigation
* routing
* session state organization
* dashboard usability
* reusable UI structures
* workflow clarity
* feedback systems
* role-based experiences

while preserving the current bakery management workflows and JSON-based architecture.
