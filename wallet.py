import json
import sys
from datetime import datetime

from wallet_const import (COMMAND_CATEGORIES, DEFAULT_FILE, HELLO, HINT_USAGE,
                          SEARCH_FILTERS)


class PersonalFinanceWallet:
    def __init__(self, wallet_file=None) -> None:
        if wallet_file:
            wallet_file = wallet_file.split('.')
            if len(wallet_file) > 1:
                wallet_file = wallet_file[: -1]
            wallet_file.append('.json')
            self.file = "".join(wallet_file)
        else:
            self.file: str = DEFAULT_FILE
        self.data: dict = self.load_data()

    def load_data(self) -> dict:
        try:
            with open(self.file, "r") as file:
                data = json.load(file)
                print("\t\t~ wallet ready ~")
        except FileNotFoundError:
            data = {"total_income": 0, "total_expenses": 0,
                    "balance": 0, "income": [], "expense": []}
            print("\t\t~ wallet empty ~")
        return data

    def save_data(self) -> None:
        with open(self.file, "w") as file:
            json.dump(self.data, file, indent=2, ensure_ascii=False)

    def print_balance(self, command) -> None:
        if len(command) < 2 or command[1] != 'balance':
            print("Usage: Wallet-> show balance")
            return
        print(f"\n\tTotal Income: \t {self.data['total_income']}")
        print(f"\tTotal Expenses:  {self.data['total_expenses']}")
        print(f"\tCurrent Balance: {self.data['balance']}", end="\n\n")

    def add_record(self, command) -> None:
        try:
            category, amount = command[1], int(command[2])
            description = "".join(command[3:])
        except IndexError:
            print("There are not enough arguments provided.")
            return
        index = len(self.data[category])
        record = {
            "id": index,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "amount": amount,
            "description": description
        }
        self.data[category].append(record)
        if category == "income":
            self.data["total_income"] += amount
            self.data["balance"] += amount
        elif category == "expense":
            self.data["total_expenses"] += amount
            self.data["balance"] -= amount
        self.save_data()
        print(f"record id: {index} - successfully added")

    def edit_record(self, command) -> None:
        try:
            category = command[1]
            index, amount = int(command[2]), int(command[3])
            description = "".join(command[4:])
        except IndexError:
            print("There are not enough arguments provided.")
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
        self.data[category][index]["date"] = datetime.now(
                                            ).strftime("%Y-%m-%d %H:%M:%S")
        self.save_data()
        print(f"record id: {index} - successfully changed")

    def _get_search_filters(self, command) -> dict[str, str]:
        query_filters = {}
        try:
            i = 1
            while i < len(command):
                if command[i] in SEARCH_FILTERS:
                    query_filters[command[i]] = command[i + 1]
                    i += 1
                i += 1
        except IndexError:
            print(f"\tAttention: filter '{command[i]}' needs value.\n")
        return query_filters

    def _amount_matching(self, query_filters, record) -> bool:
        if (
            (query_filters.get('-a') is None
                or record["amount"] != int(query_filters['-a']))
            and
            (query_filters.get('-g') is None
                or record["amount"] < int(query_filters['-g']))
            and
            (query_filters.get('-l') is None
                or record["amount"] > int(query_filters['-l']))
        ):
            return True
        return False

    def _date_matching(self, query_filters, record) -> bool:
        entity_date = record["date"].split()[0]

        if query_filters.get('-d'):
            if entity_date == query_filters['-d']:
                return False

        if query_filters.get('-p'):
            start_date, end_date = query_filters['-p'].split(':')
            if (
                entity_date >= start_date
                and entity_date <= end_date
            ):
                return False
        return True

    def _search_records(self, search_data, query_filters) -> list:
        found_records = []
        for record in search_data:
            if (
                ('-a' in query_filters or
                 '-g' in query_filters or
                 '-l' in query_filters)
                and self._amount_matching(query_filters, record)
            ):
                continue
            if (
                ('-d' in query_filters or
                 '-p' in query_filters)
                and self._date_matching(query_filters, record)
            ):
                continue
            found_records.append(record)
        return found_records

    def _print_record(self, record):
        print(
            f"\tID: {record['id']}\n",
            f"\tAmount: {record['amount']}\n",
            f"\tDate: {record['date']}\n",
            f"\tDescription: {record['description']}\n"
        )

    def _print_records(self, records, category) -> None:
        print(f"\n {category}:")
        if records:
            for entry in records:
                self._print_record(entry)
        else:
            print("\tNo records found for the provided search criteria\n")

    def search_by_filters(self, command) -> None:
        query_filters: dict[str, str] = self._get_search_filters(command)
        category: str | None = query_filters.get('-c')
        if category is not None and self.check_category(category):
            categories: tuple[str] = (category,)
        else:
            categories: tuple[str] = COMMAND_CATEGORIES
        for category in categories:
            search_data: dict = self.data[category]
            records: list = self._search_records(search_data, query_filters)
            self._print_records(records, category)

    def check_category(self, category):
        if category not in COMMAND_CATEGORIES:
            print(f"Invalid category: '{category}' -"
                  f" use '{COMMAND_CATEGORIES[0]}'"
                  f" or '{COMMAND_CATEGORIES[1]}'.")
            return False
        return True


if __name__ == '__main__':
    print(HELLO)
    wallet_file = sys.argv.pop()
    if wallet_file == __file__:
        wallet_file = None
    wallet = PersonalFinanceWallet(wallet_file)
    while True:
        command = input("Wallet-> ").split()
        if len(command) < 1:
            continue
        match command[0].lower():
            case 'show':
                wallet.print_balance(command)
            case 'add':
                if wallet.check_category(command[1]):
                    wallet.add_record(command)
            case 'edit':
                if wallet.check_category(command[1]):
                    wallet.edit_record(command)
            case 'search':
                wallet.search_by_filters(command)
            case 'serch':
                wallet.search_records(command)
            case 'exit':
                sys.exit()
            case _:
                print(f'Unknown COMMAND: "{"".join(command)}"')
                print(HINT_USAGE)
