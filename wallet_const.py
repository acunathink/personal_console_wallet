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
COMMAND_CATEGORIES = ("income", "expense")
