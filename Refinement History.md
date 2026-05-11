# Author

Prepared for: Sammy Ford

---
# Refinement History and Layer Impact Analysis

## Original Prompt

> “Make a document with all the follow up prompts i just asked , and for each refinement, explain what changed and what layer was affected?”

---

# Refinement 1

## Prompt

> “i want you to take the test Test accounts out of the code”

## What Changed

The visible demo/test account credentials were removed from the login page UI.

Removed:

* Owner test account display
* Employee test account display
* `st.code()` login examples

---

## Layer Affected

### UI Layer

File affected:

* `ui.py`

Reason:
The login account display existed entirely inside the login page rendering logic.

---

# Refinement 2

## Prompt

> “i also wan the background to be yellow and you forgot st.rerun()”

## What Changed

The application styling and refresh behavior were updated.

Added:

* yellow bakery-themed background styling
* custom CSS styling using `st.markdown()`
* additional `st.rerun()` calls after:

  * registration
  * product creation
  * CRUD operations
  * page changes

---

## Layers Affected

### App Layer

File affected:

* `app.py`

Reason:
Global styling and application-level appearance settings were added here.

---

### UI Layer

File affected:

* `ui.py`

Reason:
`st.rerun()` behavior was needed after UI-triggered actions and navigation changes.

---

# Refinement 3

## Prompt

> “what happened to my chatbot code”

## What Changed

A review identified that the original chatbot system was missing after the initial refactor.

The missing functionality included:

* chatbot UI
* chat history
* predefined bakery/business prompts
* inventory analytics responses
* revenue/order responses
* discontinued item responses

No code changes occurred in this step.

---

## Layers Identified as Missing

### UI Layer

Missing:

* chat interface
* `st.chat_input`
* `st.chat_message`

### Service Layer

Missing:

* chatbot response generation
* business intelligence logic

### App Layer

Missing:

* chatbot session persistence

---

# Refinement 4

## Prompt

> “i want all the features from my original code in the new code”

## What Changed

The missing bakery application features were restored.

Restored functionality:

* chatbot assistant
* chat history
* low stock alerts
* sales metrics
* inventory metrics
* product CRUD
* discontinued item tracking
* order creation
* owner analytics
* employee sales workflows
* inventory updates
* tabs and dashboard organization

---

## Layers Affected

### App Layer

File affected:

* `app.py`

Changes:

* chatbot session state
* application initialization
* global styling

---

### Service Layer

File affected:

* `service.py`

Changes:

* chatbot response logic
* inventory services
* order services
* analytics calculations
* CRUD operations

---

### UI Layer

File affected:

* `ui.py`

Changes:

* chatbot rendering
* owner dashboard tabs
* employee dashboard tabs
* inventory workflows
* sales workflows
* metric displays

---

### Data Layer

File affected:

* `data.py`

Changes:

* discontinued item persistence
* order retrieval
* inventory retrieval

---

# Refinement 5

## Prompt

> “i want you to make the webisite more organized and pretty like an actual webiste”

## What Changed

The UI design and layout were redesigned to improve usability and appearance.

Added:

* bakery-themed styling
* custom CSS
* improved spacing
* organized dashboard sections
* styled buttons
* improved headers
* cleaner layouts
* improved metric presentation
* grouped content areas

---

## Layers Affected

### App Layer

File affected:

* `app.py`

Reason:
Global CSS styling and theme customization were added.

---

### UI Layer

File affected:

* `ui.py`

Reason:
Dashboard organization, titles, sections, and overall page structure were redesigned.

---

# Refinement 6

## Prompt

> “why is there still no st.rerun”

## What Changed

Additional rerun behavior was identified as missing in several workflows.

The review identified missing refresh behavior after:

* page changes
* CRUD updates
* sidebar navigation
* session state updates
* inventory changes

This step clarified where reruns were still inconsistent.

---

## Layers Affected

### UI Layer

File affected:

* `ui.py`

Reason:
Most Streamlit rerun behavior occurs after user-triggered UI actions.

---

# Refinement 7

## Prompt

> “please do that”

## What Changed

Additional `st.rerun()` calls were implemented across navigation and workflows.

Added reruns after:

* page routing
* owner dashboard navigation
* employee dashboard navigation
* login navigation
* registration navigation
* session state updates

---

## Layers Affected

### UI Layer

File affected:

* `ui.py`

Reason:
The UI layer controls navigation and interaction-based reruns.

---

# Refinement 8

## Prompt

> “make sure to use Functions
> You might create functions such as:

load_json_data(...)
save_json_data(...)
find_user_by_email(...)
validate_login(...)
create_new_record(...)
update_record_status(...)
filter_records_by_user(...)
Classes
You might create classes such as:

class User:
...

class Student(User):
...

class Instructor(User):
...

class Appointment:
...

class Request:
...

class InventoryItem:
...

class DataManager:
...

class AIChatAssistant:
...
Methods
Inside your classes, you might define methods such as:

user.can_access_page(...)
request.update_status(...)
data_manager.load_records(...)
data_manager.save_records(...)
assistant.generate_response(...)”

## What Changed

The architecture was redesigned using stronger object-oriented programming practices.

Added:

* reusable functions
* reusable methods
* service classes
* inventory models
* user models
* order models
* chatbot assistant class
* centralized data manager
* reusable validation methods
* record filtering methods
* role-based access methods

---

## Layers Affected

### Data Layer

File affected:

* `data.py`

Changes:

* `DataManager`
* reusable JSON methods
* centralized persistence

---

### Service Layer

File affected:

* `service.py`

Changes:

* `User`
* `InventoryItem`
* `Order`
* `AuthService`
* `InventoryService`
* `OrderService`
* `AIChatAssistant`
* reusable methods/functions

---

### UI Layer

File affected:

* `ui.py`

Changes:

* `UIManager`
* reusable rendering methods
* centralized rendering logic

---

# Refinement 9

## Prompt

> “Make sure the code follows all this Grading Criteria”

## What Changed

The entire application was refined to align with the grading rubric.

Improvements included:

* stronger separation of concerns
* better dashboard layouts
* expanded Streamlit layout usage
* role-specific workflows
* visible demo accounts
* reusable forms
* tabs and containers
* JSON persistence improvements
* additional CRUD consistency
* cleaner navigation
* improved object-oriented architecture
* reusable methods/classes
* stronger UI organization

---

## Layers Affected

### App Layer

File affected:

* `app.py`

Changes:

* styling improvements
* application initialization
* session state management

---

### Data Layer

File affected:

* `data.py`

Changes:

* improved persistence structure
* reusable JSON handlers

---

### Service Layer

File affected:

* `service.py`

Changes:

* expanded classes
* CRUD consistency
* validation methods
* analytics methods
* chatbot methods
* filtering methods

---

### UI Layer

File affected:

* `ui.py`

Changes:

* forms
* tabs
* expanders
* columns
* containers
* role dashboards
* improved navigation
* reusable rendering methods
* improved feedback messages

---

# Final Assessment

The refinement process progressively transformed the original single-file bakery application into a layered, object-oriented Streamlit application with:

* reusable services
* centralized persistence
* cleaner UI organization
* role-based routing
* JSON persistence
* CRUD workflows
* chatbot integration
* improved rerun behavior
* stronger dashboard organization
* reusable methods/classes/functions
* grading-rubric-aligned architecture

The final structure now demonstrates:

* separation of concerns
* object-oriented programming
* reusable architecture
* layered design
* improved user experience
* maintainable Streamlit workflows.
