### Sales Analytics System

### Project Overview

This project is a Sales Analytics System developed using Python.
The purpose of this project is to read sales transaction data from a text file, clean the data by removing invalid records, fix formatting issues, and display a summary of valid and invalid records.

### The project focuses on demonstrating:

1. Python file handling
2. Data cleaning and validation
3. Modular programming using multiple Python files
4. Basic data analytics logic

### Folder Structure

Q1
|
|-- main.py
|-- README.md
|-- requirements.txt
|
|-- data
||-- sales_data.txt
|
|-- utils
||-- file_handler.py
||-- data_processor.py
||-- api_handler.py
|
|-- output

### Requirements

1. Python version 3 or above
2. No external Python libraries are required

### How to Run the Project

- Step 1: Open the Project Folder
  Open Visual Studio Code and open the folder named:
  SALES_ANALYTICS_SYSTEMS
- Step 2: Open Terminal
  In Visual Studio Code:
  Click on the Terminal menu
  Select New Terminal
- Step 3: Run the Program
  In the terminal, type the following command and press Enter:
  python -m Q1.main

### Expected Output

After running the program, the following output will be displayed on the terminal:

Total records parsed: 80
Invalid records removed: 10
Valid records after cleaning: 70

### Data Cleaning Rules Followed

Records Removed (Invalid Records):

- Records with missing CustomerID
- Records with missing Region
- Records where Quantity is less than or equal to 0
- Records where Unit Price is less than or equal to 0
- Records where TransactionID does not start with the letter "T"

Records Cleaned and Kept (Valid Records):

- Commas removed from ProductName
- Commas removed from numeric values such as Quantity and Unit Price
- Empty lines skipped

### Description of Files

1. main.py
   This is the main file that runs the entire program.
   It calls functions from other modules, processes the sales data, and prints the final output.
2. file_handler.py
   This file is responsible for reading the sales data file safely.
   It handles file reading and encoding issues.
3. data_processor.py
   This file contains logic for cleaning and validating sales data.
   It removes invalid records and fixes formatting issues.
4. api_handler.py
   This file simulates an external API call to fetch product information.
   (It is included for learning purposes.)
5. sales_data.txt
   This file contains raw sales transaction data provided in the assignment.

### Conclusion

This Sales Analytics System successfully processes raw sales data, removes invalid entries, cleans formatting issues, and displays a clear summary of results.
The project follows modular coding practices and fulfills all the requirements mentioned in the assignment.
