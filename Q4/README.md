### Q4 – API Integration

This folder contains the solution for Question 4: API Integration of the Sales Analytics System assignment.
The objective is to integrate an external API (DummyJSON), enrich sales data with product details, and save the enriched dataset to a file.

### Folder Structure

Q4
│
├── main.py
├── README.md
├── requirements.txt
│
├── data
│ └── sales_data.txt
│ └── enriched_sales_data.txt
│
├── utils
│ ├── file_handler.py
│ └── data_processor.py
| └── api_handler.py
│
└── output

### How to Run the Program

- Open Visual Studio Code
- Open the Q4 folder
- Open the terminal inside the Q4 folder
  Run:
  python -m Q4.main

### Expected Output

- API fetch success message
- Enriched data saved confirmation
- enriched_sales_data.txt generated in data folder

### Features Implemented

1. API Integration

- Fetch product data from DummyJSON API
- Handles API errors gracefully

2. Product Mapping

- Maps API product ID to category, brand, and rating

3. Data Enrichment

- Matches sales product IDs with API products
- Adds:

  a. API_Category
  b. API_Brand
  c. API_Rating
  d. API_Match flag

4. File Output

- Saves enriched data in pipe-delimited format
- Automatically creates output directory if missing

### Conclusion

This implementation fulfills all requirements for Question 4, including successful API usage, correct enrichment logic, and proper file output generation.
