# DataBase Logic Here
import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

load_dotenv()

class DataBase:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host = os.getenv("DB_HOST"),
                user = os.getenv("DB_USER"),
                password = os.getenv("DB_PASSWORD"),
                database = os.getenv("DB_NAME")
            ) 
            self.cursor = self.connection.cursor()
            self.cursor.execute("CREATE TABLE IF NOT EXISTS transactions(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), amount DOUBLE(10, 3), category VARCHAR(150), Transaction_date DATE)")
            self.connection.commit()
        except Error as e:
            print(f"Failed to connect. ERROR: {e}")
    
    def add_expense(self, obj):
        try:
            self.cursor.execute("INSERT INTO transactions (name, amount, category, Transaction_date) VALUES (%s, %s, %s, %s)", (obj.name, obj.amount, obj.category, obj.date))
            self.connection.commit()  # saves the change permanently
        except Error as e:
            print(f"Transaction Was not Stored!!!! ERROR: {e}")
        


