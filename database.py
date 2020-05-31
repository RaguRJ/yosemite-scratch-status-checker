import mysql.connector
from dotenv import load_dotenv
import os
from os.path import join, dirname

# Loading variables in .env folder
print(__file__)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Connecting to the database
def main():
    mydb = mysql.connector.connect(
        host="10.244.2.52",
        user="root",
        passwd=os.environ.get("db_passwd"),
        # database="testdb_2" # remove this if running this py for the first time
    )

    mycursor = mydb.cursor()
    # mycursor.execute("CREATE DATABASE testdb_2")
    # list all databases
    # mycursor.execute("SHOW DATABASES")
    # for db in mycursor:
    #     print(db)

    #Creating a table
    # mycursor.execute("CREATE TABLE dogs (name VARCHAR(255), age INTEGER(2))")
    
    #Displaying tables
    # mycursor.execute("SHOW TABLES")
    # for tb in mycursor:
    #     print(tb)

    #inserting data into tables
    # sql_ins = "INSERT INTO dogs (name, age) VALUES (%s, %s)"
    # fav_dog = [("caesar", 2),
    #             ("rover", 7)
    # ]

    # mycursor.executemany(sql_ins, fav_dog)
    # mydb.commit()

    # Fetching data from database
    # mycursor.execute("SELECT * FROM dogs") # you can replace * with a column name
    # result = mycursor.fetchall()
    # for row in result:
    #     print(row)
    # mycursor.execute("SELECT * FROM dogs")
    # result = mycursor.fetchone()
    # print(result)
    

    mycursor.execute("DROP DATABASE testdb_2") 

if __name__ == "__main__":
    main()