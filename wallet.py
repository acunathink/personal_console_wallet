import json
import sys


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
        self.data: dict = self.load_data()
        self.file = DEFAULT_FILE

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
        pass

    def add_record(self, command):
        pass

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
                pass
            case 'add':
                pass
            case 'edit':
                pass
            case 'search':
                pass
            case 'exit':
                sys.exit()
            case _:
                print(f'Unknown COMMAND: "{"".join(command)}"')
                print(HINT_USAGE)
