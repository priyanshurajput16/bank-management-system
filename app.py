import streamlit as st
from bank import Bank

bank = Bank()

st.set_page_config(
    page_title="Bank Management System",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Bank Management System")

menu = st.sidebar.radio(
    "Select Option",
    [
        "Create Account",
        "Deposit",
        "Withdraw",
        "View Details",
        "Update Details",
        "Delete Account"
    ]
)

# CREATE ACCOUNT

if menu == "Create Account":

    st.subheader("Create Account")

    name = st.text_input("Name")
    age = st.number_input(
        "Age",
        min_value=18,
        step=1
    )

    email = st.text_input("Email")
    pin = st.text_input(
        "PIN",
        type="password"
    )

    if st.button("Create Account"):

        success, msg = bank.create_account(
            name,
            age,
            email,
            pin
        )

        if success:
            st.success(
                f"Account Created Successfully\n\nAccount Number: {msg}"
            )
        else:
            st.error(msg)

# DEPOSIT

elif menu == "Deposit":

    st.subheader("Deposit Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    amount = st.number_input(
        "Amount",
        min_value=1
    )

    if st.button("Deposit"):

        success, msg = bank.deposit(
            acc,
            pin,
            amount
        )

        if success:
            st.success(msg)
        else:
            st.error(msg)

# WITHDRAW

elif menu == "Withdraw":

    st.subheader("Withdraw Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    amount = st.number_input(
        "Amount",
        min_value=1
    )

    if st.button("Withdraw"):

        success, msg = bank.withdraw(
            acc,
            pin,
            amount
        )

        if success:
            st.success(msg)
        else:
            st.error(msg)

# VIEW DETAILS

elif menu == "View Details":

    st.subheader("View Account")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show Details"):

        user = bank.get_details(acc, pin)

        if user:

            st.info(
                f"""
                Name : {user['name']}
                
                Age : {user['age']}
                
                Email : {user['email']}
                
                Balance : ₹{user['balance']}
                """
            )

        else:
            st.error("Invalid Credentials")

# UPDATE DETAILS

elif menu == "Update Details":

    st.subheader("Update Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("Current PIN", type="password")

    name = st.text_input("New Name")
    email = st.text_input("New Email")
    new_pin = st.text_input(
        "New PIN",
        type="password"
    )

    if st.button("Update"):

        success, msg = bank.update_details(
            acc,
            pin,
            name,
            email,
            new_pin
        )

        if success:
            st.success(msg)
        else:
            st.error(msg)

# DELETE ACCOUNT

elif menu == "Delete Account":

    st.subheader("Delete Account")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):

        success, msg = bank.delete_account(
            acc,
            pin
        )

        if success:
            st.success(msg)
        else:
            st.error(msg)