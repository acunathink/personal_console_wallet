from wallet_const import COMMAND_CATEGORIES


def check_category(category):
    if category not in COMMAND_CATEGORIES:
        print(f"Invalid category: {category}. Use 'income' or 'expense'.")
        return False
    return True
