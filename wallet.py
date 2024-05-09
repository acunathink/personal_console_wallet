import json
import sys
from datetime import datetime

from wallet_utils import check_category
from wallet_const import DEFAULT_FILE, HELLO, HINT_USAGE


class PersonalFinanceWallet:
    def __init__(self) -> None:
        self.file = DEFAULT_FILE
        self.data: dict = self.load_data()

    def load_data(self) -> dict:
        try:
            with open(self.file, "r") as file:
                data: dict = json.load(file)
                print("\t\t~ wallet ready ~")
        except FileNotFoundError:
            data: dict = {"balance": 0, "income": [], "expense": []}
            print("\t\t~ wallet empty ~")

        return data

    def save_data(self):
        with open(self.file, "w") as file:
            json.dump(self.data, file, indent=2)

    def print_balance(self, command):
        if len(command) < 2 or command[1] != 'balance':
            print("Usage: Wallet-> show balance")
            return
        total_income = sum(item["amount"] for item in self.data["income"])
        total_expenses = sum(item["amount"] for item in self.data["expense"])
        print(f"\n\tTotal Income: \t {total_income}")
        print(f"\tTotal Expenses:  {total_expenses}")
        print(f"\tCurrent Balance: {self.data['balance']}", end="\n\n")

    def add_record(self, command):
        try:
            category, amount = command[1], int(command[2])
            description = "".join(command[3:])
        except IndexError:
            print("There are not enough arguments provided.")
            return
        except Exception as ex:
            print(ex)
            return

        record = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "amount": amount,
            "description": description
        }
        self.data[category].append(record)
        if category == "income":
            self.data["balance"] += amount
        elif category == "expense":
            self.data["balance"] -= amount
        self.save_data()
        print(f"record id: {len(self.data[category])} - successfully added")

    def edit_record(self, command):
        try:
            category = command[1]
            index, amount = int(command[2]), int(command[3])
            description = "".join(command[4:])
        except IndexError:
            print("There are not enough arguments provided.")
            return
        except Exception as ex:
            print(ex)
            return
        try:
            if description:
                self.data[category][index]["description"] = description
        except IndexError:
            print(f"wrong id provided: record {index} does not exist")
            return

        if category == "income":
            self.data["balance"] -= self.data[category][index]["amount"]
            self.data["balance"] += amount
        elif category == "expense":
            self.data["balance"] += self.data[category][index]["amount"]
            self.data["balance"] -= amount

        self.data[category][index]["amount"] = amount
        self.save_data()
        print(f"record id: {len(self.data[category])} - successfully changed")

    def search_records(self, command):
        pass


if __name__ == '__main__':
    print(HELLO)
    wallet = PersonalFinanceWallet()
    while True:
        command = input("Wallet-> ").split()
        if len(command) < 1:
            continue
        match command[0]:
            case 'show':
                wallet.print_balance(command)
            case 'add':
                if check_category(command[1]):
                    wallet.add_record(command)
            case 'edit':
                if check_category(command[1]):
                    wallet.edit_record(command)
            case 'search':
                wallet.search_records(command[1:])
            case 'exit':
                sys.exit()
            case _:
                print(f'Unknown COMMAND: "{"".join(command)}"')
                print(HINT_USAGE)
