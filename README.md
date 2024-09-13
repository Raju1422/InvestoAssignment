# Investo Assignment 
## Task -1 :Data is listed in Excel/CSV   for one ticker symbol. Create a table in a database (Postgres or MySQL). Use Python to insert data into the database. 
###  Files
connection.py: This script defines functions for establishing and closing the connection to the PostgreSQL database.
insert_data.py: This script reads the CSV data file and inserts it into the specified table in the PostgreSQL database.
HINDALCO_1D.csv: The stock data file, containing datetime, open, high, low, close, and volume fields.
### Working 
This script will:
- Read the data from HINDALCO_1D.csv.
- Insert the data into the stock table in the PostgreSQL database.
- Batch insert the data in chunks of 100 records (you can adjust this in the script)
### Output 
![data in database image]("C:\Users\SANTOSH\Pictures\Screenshots\outpu1.png")

## Task - 2 : Use Python to analyze data and create an investing/trading strategy of your choice. If you are not aware of any strategy: use simple moving average crossover

### Files
HINDALCO_1D.csv: The stock data file, containing datetime, open, high, low, close, and volume fields.

investo.ipynb: The notebook file where the EMA crossover strategy is implemented and visualized

### Working 
The notebook will:

- Read the stock price data from HINDALCO_1D.csv.
- Calculate 20-day and 50-day EMAs.
- Generate buy and sell signals based on the EMA crossover strategy.
- Plot the stock's closing prices along with EMAs and the buy/sell signals.
### Key Variables:
- EMA_20: The 20-day Exponential Moving Average.
- EMA_50: The 50-day Exponential Moving Average.
- signal: 1 if EMA_20 > EMA_50 (Buy signal), 0 otherwise.
- position: Change in signal values, used to mark buy (1) and sell (-1) positions.\

### Visualizing the Strategy
The following chart will be generated by the notebook:

- Black line: Closing price of the stock.
- Blue line: 20-day EMA.
- Green line: 50-day EMA.
- Green arrows: Buy signals (when EMA_20 crosses above EMA_50).
- Red arrows: Sell signals (when EMA_50 crosses above EMA_20).
### Results
Once the notebook is executed, you'll be able to see buy and sell signals overlaid on the stock's closing price and EMA lines. This visualization helps in understanding how well the EMA crossover strategy performs over a given historical period.
### Output 
![plot image]("C:\Users\SANTOSH\Downloads\output2.png")

## Unit Testing for Trading Data Validation

The test cases ensure that the data conforms to the expected types and formats:

- Open, High, Low, and Close prices should be decimals.
- Volume should be an integer.
- Instrument should be a string.
- Datetime should be a valid datetime format.

### Files:
test.py: This file includes test cases to ensure data validity for trading information.

### Run Unit Tests:
```
python -m unittest test.py
```
### Test Cases
- test_valid_input: Verifies that the data with valid types and formats passes the validation check.
- test_invalid_input: Checks that the data with invalid types (e.g., volume as a string) raises a ValueError.

### output 
![test case]("C:\Users\SANTOSH\Pictures\Screenshots\testcase.png")