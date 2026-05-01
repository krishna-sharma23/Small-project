# Expense class
from datetime import date as dt

class Expense:
    def __init__(self, name="Unknown", amount=0.0, category="NA", date = None):
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date if date is not None else dt.today()

    def display_expense(self):
        print("********************Transaction********************")
        print(f"Transaction Name:         {self.name}")
        print(f"Amount:                   {self.amount}")
        print(f"Category:                 {self.category}")
        print(f"Date:                     {self.date}")
        print("***************************************************")