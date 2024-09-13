from connection import get_connection,close_connection
import pandas as pd
from psycopg2.extras import execute_batch
def insert_data_to_db(df,connection,table_name,chunk_size):
    try: 
        data = [tuple(x) for x in df.to_numpy()]
        columns =  df.columns.tolist()
        columns_str = ','.join(columns)
        values_str = ','.join(['%s']*len(columns))
        sql = f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str})"
        with connection.cursor() as cur:
            execute_batch(cur,sql,data,chunk_size)
            connection.commit()
        print("Successfully inserted data into db")
    except Exception as e:
       print("Unable to insert data")
       print(e)

def main(): 
    try:
        file_name="HINDALCO_1D.csv"
        table_name="stock"
        chunk_size = 100
        connection = get_connection()
        if connection:
            df = pd.read_csv(file_name,parse_dates=['datetime'],index_col=False)
            insert_data_to_db(df,connection,table_name,chunk_size)
            close_connection(connection)
        else:
            print("connection failed!!")
    except Exception as e:
        print(e)
        
if __name__ == "__main__":
    main()