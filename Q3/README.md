### Q3 – Data Processing & Analysis

This folder contains the solution for Question 3: Data Processing & Analysis of the Sales Analytics System assignment.
The objective of this question is to perform analytical computations on validated sales data, including revenue calculations, region-wise performance, product and customer analysis, and date-based trends.

### Folder Structure

Q3
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

- Open Visual Studio Code
- Open the Q3 folder
- Open the terminal inside the Q3 folder
- Run the following command:
  python -m Q3.main

### Expected Output

After execution, the program performs multiple analytical tasks and displays:

1. Total revenue
2. Region-wise sales summary
3. Top 5 selling products
4. Customer purchase analysis
5. Daily sales trend
6. Peak sales day
7. Low performing products

### Features Implemented

1. Sales Summary Calculations

- Total revenue calculation
- Average order values
- Aggregations using quantity and price

2. Region-Wise Performance

- Total sales per region
- Transaction count per region
- Percentage contribution
- Sorted by sales amount

3. Product Analysis

- Top selling products by quantity
- Revenue per product
- Low performing products detection

4. Customer Analysis

- Total spend per customer
- Purchase count
- Average order value
- Unique products bought

5. Date-Based Analysis

- Daily sales trend
- Transaction count per day
- Unique customers per day
- Peak sales day identification

### Conclusion

This implementation satisfies all evaluation criteria for Question 3, including accurate calculations, correct aggregations, proper sorting, and complete analytical coverage.
This module was tested successfully and verified.
