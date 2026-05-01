# Entry point

from model import Expense
from db import DataBase
from datetime import datetime
from datetime import date as dt


def dateformat(date):
    try:
        str_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid Format For Date!!!!!")
        return 
    return str_date

db_obj = DataBase()

while True:
    print("********************EXPENSE TRACKER********************")
    print("'a' to add Transaction")
    print("'e' to exit")
    print("*******************************************************")
    choice = input("Enter your choice: ")
    if choice == 'e':
        break
    elif choice == 'a':
        name = input('Enter the name of the Product')
        if len(name) == 0:
            print("No Name was Entered")
            continue
        try:
            amount = float(input("Enter the Amount of the item: "))
        except ValueError:
            print("Invalid Input")
            continue
        category = input("Enter the Category of the item(Groceries/Sports equipments/Clothes/etc.): ")
        date = input("When was the Transaction happened in YYYY-MM-DD format: ")
        date = dateformat(date)
        date = date if date is not None else dt.today()
        expense = Expense(name, amount, category, date)
        db_obj.add_expense(expense)


