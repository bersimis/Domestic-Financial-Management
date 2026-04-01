Development Plan & System Architecture
Welcome to the Family Finance Management application repository. This document outlines the code architecture (Screen-based Architecture with centralized data management) and the task delegation among team members.

1. Project Structure
To keep the code clean, avoid circular imports, and prevent massive, unreadable files, the project is divided into the following standalone .py files.

Core & Database
main.py: The entry point of the application. Its only job is to initialize and call login.py.

database.py: The "warehouse" of the app. It contains only SQL queries (SQLite). This is the only file that communicates directly with the database (finance.db). All other files call functions from here.

session.py: Manages the application state. It stores the ID and username of the currently logged-in user so that all other files can access them.

Authentication
login.py: The graphical user interface (Tkinter) and logic for user login. It verifies credentials via database.py and, if successful, updates session.py and opens the Dashboard.

register.py: The new user registration form. Includes necessary validations (e.g., checking if the username already exists) and secure password storage (hashing).

Main UI
dashboard.py: The main window of the application. It contains the navigation menu and acts as a "canvas" where other sub-components (graphics, forms) are loaded.

transactions.py: The form for entering new income/expenses and the main table (Treeview) displaying the current month's transactions.

categories.py: A management window (add/delete) for available income and expense categories (e.g., Salary, Electricity, Supermarket).

Data Analysis & Export
summary.py: Handles calculations (summing income, subtracting expenses) and returns the current balance and total amounts to be displayed on the Dashboard.

charts.py: Connects with the matplotlib library to create charts, which are embedded into the Tkinter interface.

export.py: Implements the project requirement for exporting user data to an Excel file (.xlsx) for further processing.

2. Tasks per person
The development of the application will be carried out in parallel by the 3 team members. Each member is assigned specific files to prevent code conflicts (merge conflicts) on GitHub.

Member 1: Core Architect & Security Lead
Takes charge of the system foundations, the database, and user security.

Files: database.py, session.py, login.py, register.py, main.py

Responsibilities:

Design SQLite tables (Users, Transactions, Categories).

Implement all SQL CRUD (Create, Read, Update, Delete) functions.

Create the Login/Register system with password validation and hashing.

Set up session.py to keep the active user in memory.

Member 2: UI & Transactions Manager
Takes charge of building the main screen and the core financial entry functionality.

Files: dashboard.py, transactions.py, categories.py

Responsibilities:

Create the main window (Dashboard) with the sidebar navigation menu.

Build the "Income / Expense Entry" form (Tkinter widgets).

Develop the dynamic table (Treeview) that displays transactions.

Connect the UI with database.py to save/read transactions.

Member 3: Data Analyst & Visuals
Takes charge of data visualization, calculations, and report generation.

Files: summary.py, charts.py, export.py

Responsibilities:

Calculate total income, expenses, and current balance.

Integrate matplotlib into Tkinter to create dynamic charts (like monthly expense analysis).

Create the functionality to export the transaction table to an Excel file.