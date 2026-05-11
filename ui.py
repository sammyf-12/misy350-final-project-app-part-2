
import streamlit as st

class UIManager:

    def __init__(
        self,
        auth_service,
        inventory_service,
        order_service,
        chatbot_service
    ):

        self.auth_service = auth_service
        self.inventory_service = inventory_service
        self.order_service = order_service
        self.chatbot_service = chatbot_service

    def reset_chat(self):

        st.session_state["messages"] = [
            {
                "role": "assistant",
                "content": "Hi! How can I help you?"
            }
        ]

    def render_sidebar(self):

        with st.sidebar:

            st.title("Sunshine Bakery")
            st.caption("Bakery Management Portal")

            st.divider()

            if st.session_state["logged_in"]:

                user = st.session_state["user"]

                st.markdown("### Current User")
                st.write(f"**Name:** {user['full_name']}")
                st.write(f"**Role:** {user['role']}")

                st.divider()

                st.markdown("### Navigation")

                if user["role"] == "Owner":

                    if st.button("Owner Dashboard", use_container_width=True):
                        st.session_state["page"] = "owner_dashboard"
                        st.rerun()

                elif user["role"] == "Employee":

                    if st.button("Employee Dashboard", use_container_width=True):
                        st.session_state["page"] = "employee_dashboard"
                        st.rerun()

                st.divider()

                if st.button("Logout", use_container_width=True):

                    st.session_state["logged_in"] = False
                    st.session_state["user"] = None
                    st.session_state["page"] = "login"
                    self.reset_chat()

                    st.rerun()

            else:

                st.markdown("### Navigation")

                if st.button("Login", use_container_width=True):
                    st.session_state["page"] = "login"
                    st.rerun()

                if st.button("Register", use_container_width=True):
                    st.session_state["page"] = "register"
                    st.rerun()

    def render_login_page(self):

        st.title("Sunshine Bakery Portal")

        with st.expander("View Demo Accounts"):

            st.code("Owner: owner@bakery.com / 123")
            st.code("Employee: employee@bakery.com / 1234")

        with st.form("login_form"):

            role = st.selectbox(
                "Role",
                ["Owner", "Employee"]
            )
            email = st.text_input("Email")
            password = st.text_input(
                "Password",
                type="password"
            )

            submitted = st.form_submit_button("Login")

        if submitted:

            user = self.auth_service.login(
                email,
                password,
                role
            )

            if user:

                st.session_state["logged_in"] = True
                st.session_state["user"] = user

                if role == "Owner":
                    st.session_state["page"] = (
                        "owner_dashboard"
                    )

                else:
                    st.session_state["page"] = (
                        "employee_dashboard"
                    )

                st.success("Login successful")
                st.rerun()

            else:
                st.error("Invalid credentials")

    def render_registration_page(self):

        st.title("Create Account")
        st.write("Create a new account for the bakery portal.")

        with st.form("register_form"):

            role = st.selectbox(
                "Role",
                ["Employee", "Owner"]
            )

            full_name = st.text_input("Full Name")
            email = st.text_input("Email")

            password = st.text_input(
                "Password",
                type="password"
            )

            submitted = st.form_submit_button(
                "Create Account"
            )

        if submitted:

            existing_user = self.auth_service.find_user_by_email(
                email
            )

            if (
                not full_name
                or not email
                or not password
            ):
                st.warning("Please complete all fields.")

            elif existing_user:
                st.error("This email already has an account.")

            else:

                with st.spinner("Creating account..."):

                    self.auth_service.register_user({
                        "full_name": full_name,
                        "email": email,
                        "password": password,
                        "role": role
                    })

                st.success("Account created successfully.")

                with st.container(border=True):

                    st.markdown("### Account Receipt")
                    st.markdown(f"**Role:** {role}")
                    st.markdown(f"**Name:** {full_name}")
                    st.markdown(f"**Email:** {email}")

                import time

                time.sleep(5)

                st.session_state["page"] = "login"
                st.rerun()

    def render_chatbot(self):

        st.subheader("AI Chat Assistant")

        with st.container(border=True):

            with st.expander("Example Questions"):

                st.write("- What items are low stock?")
                st.write("- What is the total revenue?")
                st.write("- What items are discontinued?")

            if "messages" not in st.session_state:
                st.session_state["messages"] = [
                    {
                        "role": "assistant",
                        "content": "Hi! How can I help you?"
                    }
                ]

            chat_container = st.container(height=350)

            with chat_container:

                for message in st.session_state["messages"]:

                    with st.chat_message(message["role"]):
                        st.write(message["content"])

                prompt = st.chat_input("Ask a question")

                if prompt:

                    st.session_state["messages"].append({
                        "role": "user",
                        "content": prompt
                    })

                    with st.chat_message("user"):
                        st.write(prompt)

                    with st.chat_message("assistant"):
                        with st.spinner("Thinking..."):

                            response = (
                                self.chatbot_service
                                .get_ai_response(st.session_state["messages"])
                            )

                            st.write(response)

                    st.session_state["messages"].append({
                        "role": "assistant",
                        "content": response
                    })

                    st.rerun()

    def render_owner_dashboard(self):

        left_col, right_col = st.columns([3, 1])

        with left_col:

            st.title("Owner Dashboard")

            metrics = (
                self.inventory_service
                .calculate_inventory_metrics()
            )

            sales = (
                self.order_service
                .calculate_sales_metrics()
            )

            row1 = st.columns(4)

            row1[0].metric(
                "Products",
                metrics["products"]
            )

            row1[1].metric(
                "Total Stock",
                metrics["stock"]
            )

            row1[2].metric(
                "Low Stock",
                metrics["low_stock"]
            )

            row1[3].metric(
                "Inventory Value",
                f"${metrics['value']:.2f}"
            )

            row2 = st.columns(3)

            row2[0].metric("Sales", sales["sales"])
            row2[1].metric("Units", sales["units"])
            row2[2].metric(
                "Revenue",
                f"${sales['revenue']:.2f}"
            )

            tabs = st.tabs([
                "Inventory",
                "Add Product",
                "Update Price",
                "Restock Product",
                "Delete Product",
                "Orders"
            ])

            inventory = (
                self.inventory_service.get_inventory()
            )

            with tabs[0]:

                for item in inventory:

                    with st.container(border=True):

                        cols = st.columns([4, 1])

                        with cols[0]:

                            st.markdown(
                                f"""
                                **{item['name']}**

                                Price: ${item['price']:.2f}  
                                Stock: {item['stock']}
                                """
                            )

                        with cols[1]:

                            if item["stock"] <= 5:
                                st.warning("Low")
                            else:
                                st.success("In Stock")


            with tabs[1]:

                st.subheader("Add Product")

                with st.form("add_product"):

                    name = st.text_input("Product Name")

                    price = st.number_input(
                        "Price",
                        min_value=0.0
                    )

                    stock = st.number_input(
                        "Stock",
                        min_value=0
                    )

                    submitted = (
                        st.form_submit_button(
                            "Add Product"
                        )
                    )

                if submitted:

                    if not name:

                        st.warning("Please enter a product name.")

                    else:

                        with st.spinner("Adding product..."):

                            new_product = {
                                "name": name,
                                "price": price,
                                "stock": stock
                            }

                            self.inventory_service.create_new_record(
                                new_product
                            )

                        st.success("Product added successfully.")

                        with st.container(border=True):

                            st.markdown("### Product Added")

                            st.markdown(f"**Name:** {name}")
                            st.markdown(f"**Price:** ${price:.2f}")
                            st.markdown(f"**Stock:** {stock}")

                        import time
                        
                        time.sleep(5)

                        st.rerun()

            with tabs[2]:

                st.subheader("Update Price")

                names = [
                    item["name"]
                    for item in inventory
                ]

                if names:

                    selected = st.selectbox(
                        "Select Product",
                        names,
                        key="update_price_product"
                    )

                    selected_item = None

                    for item in inventory:
                        if item["name"] == selected:
                            selected_item = item

                    old_price = selected_item["price"]

                    new_price = st.number_input(
                        "New Price",
                        min_value=0.0
                    )

                    if st.button("Update Price"):

                        self.inventory_service.update_record_status(
                            selected,
                            new_price,
                            0
                        )

                        st.success("Product price updated.")

                        with st.container(border=True):

                            st.markdown("### Price Update Receipt")

                            st.markdown(f"**Product:** {selected}")
                            st.markdown(f"**Previous Price:** ${old_price:.2f}")
                            st.markdown(f"**Updated Price:** ${new_price:.2f}")

                        import time

                        time.sleep(5)

                        st.rerun()

                else:
                    st.info("No products available to update.")

            with tabs[3]:

                st.subheader("Restock Product")

                names = [
                    item["name"]
                    for item in inventory
                ]

                if names:

                    selected = st.selectbox(
                        "Select Product",
                        names,
                        key="restock_product"
                    )

                    restock = st.number_input(
                        "Quantity to Add",
                        min_value=1
                    )

                    if st.button("Restock Product"):

                        selected_item = None

                        for item in inventory:
                            if item["name"] == selected:
                                selected_item = item

                        old_stock = selected_item["stock"]

                        self.inventory_service.update_record_status(
                            selected,
                            selected_item["price"],
                            restock
                        )

                        st.success("Product restocked.")

                        with st.container(border=True):

                            st.markdown("### Restock Receipt")

                            st.markdown(f"**Product:** {selected}")
                            st.markdown(f"**Previous Stock:** {old_stock}")
                            st.markdown(f"**Quantity Added:** {restock}")
                            st.markdown(f"**New Stock:** {old_stock + restock}")

                        import time

                        time.sleep(5)

                        st.rerun()

                else:
                    st.info("No products available to restock.")

            with tabs[4]:

                st.subheader("Delete Product")

                names = [
                    item["name"]
                    for item in inventory
                ]

                if names:
                    st.warning(
                        "Deleting a product will move it to the discontinued list."
                    )

                    selected = st.selectbox(
                        "Select Product",
                        names,
                        key="delete_box"
                    )

                    selected_item = None

                    for item in inventory:
                        if item["name"] == selected:
                            selected_item = item

                    if st.button("Delete Product"):

                        deleted_price = selected_item["price"]
                        deleted_stock = selected_item["stock"]

                        self.inventory_service.delete_product(
                            selected
                        )

                        st.success("Product deleted.")

                        with st.container(border=True):

                            st.markdown("### Deletion Receipt")

                            st.markdown(f"**Deleted Product:** {selected}")
                            st.markdown(f"**Price:** ${deleted_price:.2f}")
                            st.markdown(f"**Remaining Stock Before Deletion:** {deleted_stock}")
                            st.markdown("**Status:** Moved to discontinued items")

                        import time

                        time.sleep(5)

                        st.rerun()

                else:
                    st.info("No products available to delete.")

            with tabs[5]:

                st.subheader("Orders")

                orders = (
                    self.order_service.get_all_orders()
                )

                if orders:

                    for order in orders:

                        with st.container(border=True):

                            st.markdown(
                                f"""
                                **Order {order['order_id']}**

                                Customer: {order['customer']}  
                                Item: {order['item']}  
                                Quantity: {order['quantity']}  
                                Total: ${order['total']:.2f}  
                                Status: {order['status']}
                                """
                            )

                else:
                    st.info("No orders yet.")

        with right_col:

            self.render_chatbot()


    def render_employee_dashboard(self):

        left_col, right_col = st.columns([3, 1])

        with left_col:

            st.title("Employee Dashboard")

            inventory = (
                self.inventory_service.get_inventory()
            )

            tabs = st.tabs([
                "Catalog",
                "Sales",
                "Low Stock"
            ])

            with tabs[0]:

                for item in inventory:

                    with st.container(border=True):

                        cols = st.columns([4, 1])

                        with cols[0]:

                            st.markdown(
                                f"""
                                **{item['name']}**

                                Price: ${item['price']:.2f}  
                                Stock: {item['stock']}
                                """
                            )

                        with cols[1]:

                            if item["stock"] <= 5:
                                st.warning("Low")
                            else:
                                st.success("In Stock")

            with tabs[1]:

                st.subheader("Log Sale")

                item_names = [
                    item["name"]
                    for item in inventory
                ]

                if item_names:

                    with st.form("sales_form"):

                        selected = st.selectbox(
                            "Select Item",
                            item_names
                        )

                        quantity = st.number_input(
                            "Quantity Sold",
                            min_value=1
                        )

                        submitted = (
                            st.form_submit_button(
                                "Log Sale"
                            )
                        )

                    if submitted:

                        selected_item = None

                        for item in inventory:
                            if item["name"] == selected:
                                selected_item = item

                        old_stock = selected_item["stock"]
                        item_price = selected_item["price"]
                        total_price = item_price * quantity

                        with st.spinner("Logging sale..."):

                            success = (
                                self.order_service
                                .create_new_record(
                                    selected,
                                    quantity
                                )
                            )

                        if success:

                            st.success("Sale logged successfully.")

                            with st.container(border=True):

                                st.markdown("### Sale Receipt")

                                st.markdown(f"**Item:** {selected}")
                                st.markdown(f"**Quantity Sold:** {quantity}")
                                st.markdown(f"**Price Per Item:** ${item_price:.2f}")
                                st.markdown(f"**Total Sale:** ${total_price:.2f}")
                                st.markdown(f"**Previous Stock:** {old_stock}")
                                st.markdown(
                                    f"**Remaining Stock:** {old_stock - quantity}"
                                )

                            import time

                            time.sleep(5)

                            st.rerun()

                        else:
                            st.error("Insufficient stock.")

                else:
                    st.info("No products available to sell.")

            with tabs[2]:

                low_stock = [
                    item for item in inventory
                    if item["stock"] <= 5
                ]

                if low_stock:

                    for item in low_stock:

                        with st.container(border=True):

                            cols = st.columns([4, 1])

                            with cols[0]:

                                st.markdown(
                                    f"""
                                    **{item['name']}**

                                    Price: ${item['price']:.2f}  
                                    Stock: {item['stock']}
                                    """
                                )

                            with cols[1]:

                                st.warning("Low")

                else:
                    st.success("No low stock items")

        with right_col:

            self.render_chatbot()


    def render_application(self):

        self.render_sidebar()

        page = st.session_state["page"]

        if page == "login":
            self.render_login_page()

        elif page == "register":
            self.render_registration_page()

        elif page == "owner_dashboard":
            self.render_owner_dashboard()

        elif page == "employee_dashboard":
            self.render_employee_dashboard()
