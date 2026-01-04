### Q2 – Data File Handler & Preprocessing

This folder contains the solution for Question 2: Data File Handler & Preprocessing (File I/O & Error Handling) of the Sales Analytics System assignment.

The objective of this question is to read sales data safely from a text file, clean and parse the data, validate transactions based on given rules, display available filtering options, and generate a correct summary.

### Folder Structure

Q2
│
├── main.py
├── README.md
├── requirements.txt
├── **init**.py
│
├── data
│ └── sales_data.txt
│
├── utils
│ ├── file_handler.py
│ └── data_processor.py
| └── **init**.py
| └── api_handler.py
│
└── output

### How to Run the Program

1. Open Visual Studio Code
2. Open the Q2 folder
3. Open the terminal inside the Q2 folder
4. Run the following command:
   python -m Q2.main

### Expected Output

After running the program, the following information will be displayed:

- Available regions for filtering
- Transaction amount range (minimum and maximum)
- Total input records
- Invalid records count
- Final valid records count

### Sample output:

Available regions: ['East', 'North', 'South', 'West']
Transaction amount range: 257.0 to 818960.0
Total input records: 80
Invalid records: 10
Final valid records: 70

### Features Implemented

1. File Handling

- Reads non-UTF-8 encoded files
- Handles multiple encodings (utf-8, latin-1, cp1252)
- Handles FileNotFoundError
- Skips header row and empty lines

2. Data Parsing & Cleaning

- Parses pipe-delimited data
- Removes commas from product names
- Removes commas from numeric values
- Converts Quantity to integer
- Converts UnitPrice to float
- Skips malformed rows

3. Data Validation

- Quantity must be greater than 0
- UnitPrice must be greater than 0
- TransactionID must start with 'T'
- ProductID must start with 'P'
- CustomerID must start with 'C'
- Region must not be empty

4. Filtering & Summary

- Displays available regions
- Displays transaction amount range
- Supports optional filters by region and amount
- Returns correct summary counts

### Conclusion

This implementation satisfies all evaluation criteria for Question 2, including proper file handling, data cleaning, validation, filtering logic, display of available options, and correct summary output.

The solution is modular, readable, and ready for evaluation.
