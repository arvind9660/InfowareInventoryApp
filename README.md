# InfowareInventoryApp

This is an Inventory Management Desktop Application developed using PySide6 and SQLite as part of an internship assignment for InfowareIndia.com.

## Features

- Login system for operator-level access
- Product Master Form to add and manage product details
- Goods Receiving Form to enter received inventory
- Sales Form to record sales transactions
- Uses a local SQLite database (can be replaced with MySQL)
- Upload product images
- Automatic calculation of total and tax
- Project can be compiled into a Windows executable (.exe)

## Technologies Used

- Frontend: PySide6 (Python Qt6 GUI)
- Backend: Python 3.10 or above
- Database: SQLite (can be replaced with MySQL)

## Operator Login Details

Username: arvind  
Password: pass123

Username: operator2  
Password: pass456

## How to Run

1. Install dependencies

   pip install PySide6

2. Run the application

   python main.py

3. (Optional) To create an exe file

   pyinstaller --noconfirm --onefile --windowed main.py

## Folder Structure

InfowareInventoryApp  
│  
├── main.py                - Main entry point  
├── login.py               - Login form  
├── dashboard.py           - Dashboard after login  
├── product.py             - Product Master form  
├── receiving.py           - Goods Receiving form  
├── sales_form.py          - Sales form  
├── database.py            - Database connection and schema  
├── assets/                - Static folder for images  
│   └── product_images/    - Folder to store product images  
├── inventory.db           - Local SQLite database  
└── README.md              - Project information file

## Demo and GitHub Link

Demo video: Add your Google Drive or YouTube video link here  
GitHub link: https://github.com/arvind9660/InfowareInventoryApp

## Submitted By

Arvind Singh  
Internship Project for InfowareIndia.com  
