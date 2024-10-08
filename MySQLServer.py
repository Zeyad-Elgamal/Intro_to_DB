import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establishing connection to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',     # Replace with your MySQL username
            password='your_password'  # Replace with your MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # SQL query to create the database (if not exists)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            # Confirm the creation
            print("Database 'alx_book_store' created successfully!")
    
    # Explicitly catching mysql.connector.Error
    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
