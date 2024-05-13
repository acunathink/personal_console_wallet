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
        search [FILTERS] - shows list of records corresponding by FILTERS:
            -c [income|expense] - filter by category
            -a <amount> - filter by equal amount
            -g <amount> - filter by greater amount
            -l <amount> - filter by lower amount
            -d <date> - filter by date
            -p <date:date> - filter by period behind two dates
            * all filters may be use together with others
            example usage: search -с income -a 25 -g 30 -l 10 -d 2024-05-02\n
    '''
)
SEARCH_FILTERS = ('-c', '-a', '-g', '-l', '-d', '-p')
COMMAND_CATEGORIES = ('income', 'expense')
DEFAULT_FILE = "data.json"
