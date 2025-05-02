# Restaurant Ordering System 🍽️. 

A simple command-line based Restaurant Ordering System implemented in Python using CSV files to manage menu data, admin login, and customer orders.

## 📋 Features

### 👨‍💼 Admin Panel
- Admin login via `adminfile.csv`
- Add new menu items
- Remove existing items
- Update price and quantity of items
- View full menu

### 🧑‍🍳 Customer Panel
- View available menu items
- Buy items (adds to a customer order file)
- View your current order
- Update your order (add or remove items)

## 📂 File Structure

- `adminfile.csv` – Stores admin username and password
- `menu_file.csv` – Stores menu items (name, price, quantity)
- `customerFile.csv` – Stores customer orders
- `tempfile.csv` / `temp_file.csv` – Temporary files used during update/delete operations

## ▶️ How to Run

1. Make sure Python is installed on your system.
2. Create a CSV file named `adminfile.csv` with at least one admin user. Format:
``` csv
admin_username,admin_password
```
3. Run the script:
```bash
python yourscriptname.py
```

Follow on-screen prompts to interact as an admin or customer.

🛠️ Dependencies
Python standard libraries:
```
csv
os
```
No third-party libraries required.

## 🔒 Notes

Ensure the CSV files exist before running the script or add file creation checks.
This script runs in an infinite loop; restart to switch between users.
Make sure the file names (like Menu_file.csv vs menu_file.csv) match correctly – it’s case-sensitive.

## 🚀 Future Improvements
Add password hashing for admin credentials
Store orders per customer instead of a single customer file
Add exception handling for input and file errors
Implement GUI using Tkinter or PyQt
