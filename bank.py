import json
import random
import string
from pathlib import Path


class Bank:
    DATABASE = "data.json"

    def __init__(self):
        self.data = self.load_data()

    def load_data(self):
        if Path(self.DATABASE).exists():
            with open(self.DATABASE, "r") as f:
                return json.load(f)
        return []

    def save_data(self):
        with open(self.DATABASE, "w") as f:
            json.dump(self.data, f, indent=4)

    def generate_account_number(self):
        while True:
            acc = "".join(
                random.choices(
                    string.ascii_uppercase + string.digits,
                    k=8
                )
            )

            exists = any(
                user["accountNo"] == acc
                for user in self.data
            )

            if not exists:
                return acc

    def create_account(self, name, age, email, pin):

        if age < 18:
            return False, "Age must be 18+"

        if len(pin) != 4 or not pin.isdigit():
            return False, "PIN must contain exactly 4 digits"

        account_no = self.generate_account_number()

        user = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo": account_no,
            "balance": 0
        }

        self.data.append(user)
        self.save_data()

        return True, account_no

    def authenticate(self, account_no, pin):

        for user in self.data:
            if (
                user["accountNo"] == account_no
                and user["pin"] == pin
            ):
                return user

        return None

    def deposit(self, account_no, pin, amount):

        user = self.authenticate(account_no, pin)

        if not user:
            return False, "Invalid credentials"

        if amount <= 0:
            return False, "Amount must be greater than 0"

        user["balance"] += amount
        self.save_data()

        return True, f"₹{amount} deposited"

    def withdraw(self, account_no, pin, amount):

        user = self.authenticate(account_no, pin)

        if not user:
            return False, "Invalid credentials"

        if amount <= 0:
            return False, "Invalid amount"

        if user["balance"] < amount:
            return False, "Insufficient balance"

        user["balance"] -= amount
        self.save_data()

        return True, f"₹{amount} withdrawn"

    def get_details(self, account_no, pin):

        return self.authenticate(account_no, pin)

    def update_details(
        self,
        account_no,
        pin,
        new_name,
        new_email,
        new_pin
    ):

        user = self.authenticate(account_no, pin)

        if not user:
            return False, "Invalid credentials"

        if new_name:
            user["name"] = new_name

        if new_email:
            user["email"] = new_email

        if new_pin:
            if len(new_pin) != 4 or not new_pin.isdigit():
                return False, "PIN must be 4 digits"

            user["pin"] = new_pin

        self.save_data()

        return True, "Details Updated"

    def delete_account(self, account_no, pin):

        user = self.authenticate(account_no, pin)

        if not user:
            return False, "Invalid credentials"

        self.data.remove(user)
        self.save_data()

        return True, "Account deleted"