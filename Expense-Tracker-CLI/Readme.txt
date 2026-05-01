# Expense Tracker CLI

A command line expense tracking application built with Python and MySQL. Add, view, update, and delete your daily transactions directly from the terminal.

---

## Tech Stack

- Python 3
- MySQL
- mysql-connector-python
- python-dotenv

---

## Project Structure

```
expense_tracker/
├── main.py          # Entry point, handles user input and program flow
├── model.py         # Expense class — data model
├── db.py            # Database class — all MySQL logic
├── .env.example     # Template for environment variables
├── requirements.txt # Project dependencies
└── README.md
```

---

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/yourusername/expense-tracker-cli.git
cd expense-tracker-cli
```

### 2. Create and activate a virtual environment

```
python -m venv env
```

On Windows:
```
env\Scripts\activate
```

On Mac/Linux:
```
source env/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Set up MySQL

Make sure MySQL is running on your machine. Create a database named `expenses`:

```sql
CREATE DATABASE expenses;
```

### 5. Configure environment variables

Create a `.env` file in the project root by copying the example file:

```
cp .env.example .env
```

Open `.env` and fill in your MySQL credentials:

```
DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=expenses
```

The application will automatically create the required table on first run.

### 6. Run the application

```
python main.py
```

---

## Usage

```
********************EXPENSE TRACKER********************
'a' to add Transaction
'e' to exit
*******************************************************
```

Follow the prompts to enter transaction name, amount, category, and date.

Date format: `YYYY-MM-DD` — leave blank to use today's date automatically.

---

## Important

Never share or commit your `.env` file. It is listed in `.gitignore` and should stay local on your machine only.

---

## Author

Krishna
