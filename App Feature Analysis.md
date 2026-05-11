# Author

Prepared for: Sammy Ford

---
# App Features Analysis

## Original Prompt

> “I want you to review the current app features of the website. This is separate from the project structure analysis. Please study what the app currently does. This is an analysis only document and should identify current features, missing features, and incomplete workflows, usability issues, and areas that need improvement. Please name the file App Features Analysis. Record the original prompt at the top of the file you create and label it Original Prompt, all prompts asked afterward should be stored on the file under the Original Prompt at the top of the page.”

### Additional Prompts

> “Please make the document concise and remove redundancy.”

---

# Files Reviewed

* `FinalProject(4).py`
* `inventory(4).json`
* `orders(4).json`
* `users(4).json`
* `discontinued_items(4).json`

---

# Application Overview

The Sunshine Bakery and Shop website is a Streamlit-based bakery management application focused on:

* authentication
* inventory management
* sales tracking
* analytics dashboards
* chatbot assistance
* JSON-based persistence

The application currently functions more as an internal management dashboard than a public ecommerce platform.

---

# Current Features

# 1. Authentication System

## Existing Features

* Owner login
* Employee login
* User registration
* Role-based dashboard access
* Session state login persistence

## Current Issues

* Passwords stored in plain text
* No password recovery
* No session expiration
* No account/profile management
* No email verification
* Registration allows unrestricted Owner creation
* No login protection or validation rules

---

# 2. Owner Dashboard

## Existing Features

* Inventory metrics
* Sales metrics
* Inventory management
* Product creation
* Price updates
* Restocking
* Product deletion/discontinuation
* Recent sales display
* Chatbot assistant

## Current Issues

* No search or filtering
* No product categories or images
* No inventory history tracking
* No bulk inventory actions
* No export/report tools
* No confirmation dialogs before deletion
* Dashboard layout may become cluttered with larger inventories

---

# 3. Employee Dashboard

## Existing Features

* Product catalog viewer
* Daily sales logging
* Automatic stock reduction
* Low stock monitoring
* Chatbot assistant

## Current Issues

* No checkout/cart workflow
* No receipts
* No order editing/cancelation
* No payment workflow
* No customer management
* No employee activity tracking
* No search/filter functionality
* No sales timestamps

---

# 4. Chatbot Assistant

## Existing Features

Supports predefined questions about:

* low stock
* sales revenue
* order count
* most popular items
* discontinued items

## Current Issues

* Only supports exact prompts
* No natural language processing
* No AI integration
* Duplicate implementation across dashboards
* Limited business intelligence capability

---

# 5. Inventory System

## Existing Features

* Inventory creation
* Stock management
* Inventory updates
* Low stock alerts
* Discontinued item tracking

## Current Issues

* No SKU system
* No product descriptions
* No supplier/vendor tracking
* No inventory audit logs
* No forecasting/reorder tools
* No categories or sorting
* No multi-location support

---

# 6. Sales and Orders System

## Existing Features

* Sales logging
* Revenue calculation
* Order storage
* Inventory synchronization

## Current Issues

* No timestamps/dates
* No tax or discount support
* No refunds/cancellations
* No multiple-item orders
* No reporting by date range
* No payment status tracking
* No order filtering/search

---

# 7. Navigation and User Experience

## Existing Features

* Sidebar navigation
* Dashboard tabs
* Simple layouts
* Clear metric visibility

## Current Issues

* Limited responsiveness/mobile support
* Repeated UI sections
* Minimal accessibility support
* Weak visual hierarchy
* No theme customization
* Navigation scalability concerns

---

# 8. Data and Persistence

## Existing Features

Uses JSON files for:

* users
* inventory
* orders
* discontinued items

## Current Issues

* No database system
* No validation layer
* No backup/recovery system
* Direct file overwrite risks
* Difficult scalability
* No concurrency protection

---

# Missing Features

## High Priority

* Password hashing/security
* Search and filtering
* Order timestamps
* Checkout/payment workflow
* Validation improvements
* Error handling improvements
* Reporting tools
* Product categories/images

## Medium Priority

* Receipt generation
* Inventory audit logs
* Export/import tools
* Supplier tracking
* Mobile responsiveness
* Improved chatbot capabilities

## Low Priority

* Dark mode
* Notifications/alerts
* Barcode scanning
* AI recommendations
* Public storefront

---

# Incomplete Workflows

## Registration Workflow

Missing:

* email validation
* password requirements
* approval/admin controls

## Sales Workflow

Missing:

* checkout confirmation
* payment handling
* receipts
* cart system

## Inventory Workflow

Missing:

* inventory history
* product editing tools
* reorder recommendations

## User Management Workflow

Missing:

* profile editing
* role management
* account deletion

---

# Areas Needing Improvement

## Security

* password protection
* session security
* role restrictions
* input validation

## Scalability

* modular architecture
* reusable components
* improved persistence system

## User Experience

* responsive layouts
* cleaner navigation
* improved dashboard organization
* reduced duplication

## Business Functionality

* advanced order workflows
* customer management
* analytics/reporting tools

---

# Final Assessment

The application is a functional bakery management prototype with working authentication, inventory tracking, sales logging, and dashboard analytics.

The main limitations involve:

* security weaknesses
* simplified workflows
* missing reporting tools
* limited scalability
* incomplete order/customer systems
* duplicated UI logic

The application is suitable for demonstration or small internal use, but additional workflow completion, security improvements, and usability enhancements are needed before production deployment.
