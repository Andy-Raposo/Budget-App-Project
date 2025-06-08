class Category:
    """
    Class Category, that will store and process both ledger's output and the logic of deposits, expenses, transfers and balance
    """

    def __init__(self, category):
        # Initialize the category with a name and an empty ledger
        self.category = category
        self.ledger = []


    def __str__(self):
         # Prepare the title line with centered category name and asterisks variably depending on the item
        len_middle_1 = 30 - len(self.category)
        len_left_1 = len_middle_1 // 2
        len_right_1 = len_middle_1 - len_left_1
        left_1 = len_left_1 * '*'
        right_1 = len_right_1 * '*'
        middle_1 = self.category
        title = left_1 + middle_1 + right_1
        
        # Formats each ledger entries with description and amount aligned following a strict output formatting
        outcome = ''
        for item in self.ledger: 
            description = item['description'][:23]
            left = description + (' ' * (23 - len(description)))
            amount = f"{item['amount']:.2f}"
            right = amount.rjust(7)
            outcome += left + right + '\n'

        # Shows the total balance at the end of the output, with 2 decimals
        total = f"Total: {self.get_balance():.2f}"
        return title + '\n' + outcome + total


    def deposit(self, amount, description=""):
        # Appends a deposit transaction to the ledger
        self.ledger.append({'amount': amount, 'description': description})
    

    def withdraw(self, amount, description=""):
        # Checks if it's possible withdraw an specified amount of funds
        if self.check_funds(amount):
            # It appends the value to the ledger if funds are available
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        
        else:
            # Returns a warning
            print('Withdrawal impossible: Not enough funds available.')
            return False


    def get_balance(self):
        # Calculates and return the current balance
        return sum(item['amount'] for item in self.ledger)


    def transfer(self, amount, category):
        # Transfers specified funds to another category if there are enough funds
        if self.check_funds(amount):
            # Appends the values to the ledger if the transfer is possible
            self.ledger.append({'amount': -amount, 'description': f'Transfer to {category.category}'})
            category.ledger.append({'amount': amount, 'description': f'Transfer from {self.category}'})
            return True
        
        else:
            # Returns a warning
            print('Transfer impossible: Not enough funds available.')
            return False
    

    def check_funds(self, amount):
        # (it's a supporting method) Checks if the amount is available in the current balance 
        if amount > self.get_balance():
            return False
        return True



def create_spend_chart(categories):
    # Stores information off the ledger from Category to know the total spending per category
    category_spending = []
    total_spent = 0

    # Loops categories to obtain expenses
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item['amount'] < 0:
                spent += -item['amount']
        category_spending.append({"name": category.category, "spent": spent})
        total_spent += spent

    # Calculates the previous spending's percentages, rounded down to nearest 10 for formatting
    category_percentages = []
    for item in category_spending:
        percentage = (item['spent'] / total_spent) * 100
        percentage_rounded = (percentage // 10) * 10
        category_percentages.append({"name": item['name'], "percent": percentage_rounded})

    # Structure necessary to build the vertical bar chart string
    chart = 'Percentage spent by category\n'
    percentage_list = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
    for percentage in percentage_list:
        line = str(percentage).rjust(3) + '| '
        for item in category_percentages:
            if item['percent'] >= percentage:
                line += 'o  '
            else:
                line += '   '
        line += '\n'
        chart += line
    
    # Addsthe horizontal separator line between percentage output and categories
    chart += '    ' + ('---' * len(category_percentages)) + '-\n'

    # Adds the category names vertically below the chart, aligned
    line_length = max(len(item['name']) for item in category_percentages)
    for i in range(line_length):
        chart += '     '
        for item in category_percentages:
            if i < len(item['name']):
                chart += f"{item['name'][i]}  "
            else:
                chart += '   '
        chart += '\n' if i < line_length - 1 else ''

    return chart