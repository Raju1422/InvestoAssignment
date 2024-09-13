import psycopg2

def get_connection():
    try :
        connection = psycopg2.connect(
            user="Santosh",
            password="sanju@169",
            host="localhost",
            port ="5432",
            database ="Invsto"
        )
        return connection
    except Exception as e:
        print(e)
    return None

def close_connection(connection):
    if connection:
        connection.close()
        print("PostgreSQL connection is closed")

if __name__ == "__main__":
    connection = get_connection()  
    if connection:
        close_connection(connection)  