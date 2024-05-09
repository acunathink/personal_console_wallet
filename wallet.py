import json
import sys
from datetime import datetime


HELLO = "Wallet - application for accounting personal income and expenses"
HINT_USAGE = (
    '''
    Usage: Wallet-> [COMMAND] [OPTIONS]

    COMMANDS:
        show balance - shows the total income, total expenses and
                       balance between total income and total expenses\n
        add [OPTION] - adds record with OPTIONS:
             income  <amount> "description" - adds income  record
             expense <amount> "description" - adds expense record\n
        edit [OPTION] - edit record by id with OPTIONS:
              income  <id> <amount> "description" - adds income  record
              expense <id> <amount> "description" - adds expense record\n
        search [OPTION] [OPTION] [OPTION]
            OPTIONS:
                -i <income>
                -e <expense>
                -d <date>\n
    exit - quit programm
    '''
)
DEFAULT_FILE = "data.json"


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
            data: dict = {"balance": 0, "income": [], "expenses": []}
            print("\t\t~ wallet empty ~")

        return data

    def save_data(self):
        with open(self.file, "w") as file:
            json.dump(self.data, file, indent=2)

    def print_balance(self, command):
        if len(command) < 2 or command[1] != 'balance':
            print(HINT_USAGE)
            return
        total_income = sum(item["amount"] for item in self.data["income"])
        total_expenses = sum(item["amount"] for item in self.data["expenses"])
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
        if category not in ("income", "expense"):
            print(f"Invalid category: {category}. Use 'income' or 'expense'.")
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

    def edit_record(self, category, index, amount, description):
        pass

    def search_records(self, category=None, date=None, amount=None):
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
                wallet.add_record(command)
            case 'edit':
                pass
            case 'search':
                pass
            case 'exit':
                sys.exit()
            case _:
                print(f'Unknown COMMAND: "{"".join(command)}"')
                print(HINT_USAGE)
