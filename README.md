## Budget App - Category Ledger and Spending Chart

This Python project, which I designed to complete freeCodeCamp's curriculum, implements a Category class to manage budget categories with deposits, withdrawals, transfers, and balance tracking. It also includes a create_spend_chart function that generates a text-based bar chart visualizing the percentage spent per category.

## Features

- Create budget categories (e.g., Food, Clothing) with individual ledgers
- Deposit funds with optional descriptions
- Withdraw funds if balance permits, tracking spending
- Transfer funds between categories with clear transaction notes
- Get current balance of each category
- Generate a spending chart showing percentage spent by category, displayed as a vertical bar chart with category names written vertically below

## Usage

```
# Initialize categories
entertainment = Category('Entertainment')
utilities = Category('Utilities')
groceries = Category('Groceries')

# Add deposits
entertainment.deposit(1500, 'monthly allowance')
utilities.deposit(800, 'utility bill payment')
groceries.deposit(1000, 'weekly shopping')

# Save withdrawals
entertainment.withdraw(200.50, 'concert tickets')
utilities.withdraw(100.75, 'electricity bill')
groceries.withdraw(250.40, 'food and supplies')

# Transfer funds
groceries.transfer(100, entertainment)

# Display ledger for Entertainment
print(entertainment)

# Create and display spending chart
print(create_spend_chart([entertainment, utilities, groceries]))
```

## Example Output

```
********Entertainment*********
monthly allowance      1500.00
concert tickets        -200.50
Transfer from Groceries 100.00
Total: 1399.50
```

```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60|          
 50|       o  
 40|       o  
 30| o     o  
 20| o     o  
 10| o  o  o  
  0| o  o  o  
    ----------
     E  U  G
     n  t  r
     t  i  o
     e  l  c
     r  i  e
     t  t  r
     a  i  i
     i  e  e
     n  s  s
     m
     e
     n
     t
```


## Project Goal

This project is part of a learning path in Python programming, currently through a curriculum in freeCodeCamp, focusing on object-oriented design, string formatting, and algorithmic thinking. It demonstrates:

- Handling financial transactions with data visualisation
- Working with lists and dictionaries
- The use of classes and objects
- Formatting console output, including vertical text display, cleanly
