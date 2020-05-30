import mysql.connector
from dotenv import load_dotenv
import os
from os.path import join, dirname

# Loading variables in .env folder
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Connecting to the database
def main():
    mydb = mysql.connector.connect(
        host="10.244.2.52",
        user="root",
        passwd=os.environ.get("db_passwd"),
        database="testdb" # remove this if running this py for the first time
    )

    mycursor = mydb.cursor()
    #mycursor.execute("CREATE DATABASE testdb")
    #list all databases
    # mycursor.execute("SHOW DATABASES")
    # for db in mycursor:
    #     print(db)

    #Creating a table
    #mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(3))")
    
    #Displaying tables
    # mycursor.execute("SHOW TABLES")
    # for tb in mycursor:
    #     print(tb)

    #inserting data into tables
    # sql_ins = "INSERT INTO students (name, age) VALUES (%s, %s)"
    # fav_student = [("ragu", 26),
    #                 ("marshal", 67),
    #                 ("dhivya", 27),
    #                 ("deepu", 26)                
    # ]

    # mycursor.executemany(sql_ins, fav_student)
    mydb.commit()

    # Fetching data from database
    mycursor.execute("SELECT * FROM students") # you can replace * with a column name
    result = mycursor.fetchall()
    for row in result:
        print(row)
    result = mycursor.fetchone()
    print(result)
    


if __name__ == "__main__":
    main()