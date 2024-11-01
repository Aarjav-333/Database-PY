import pymysql

try:
    connection = pymysql.connect(
        host='',
        user='',
        password='',
        database=""
    )

    cursor = connection.cursor()

    create_table_query = """
    CREATE TABLE Sailor (
        S_id INT PRIMARY KEY,
        S_name VARCHAR(100),
        age INT,
        rating INT
    );
    """
    cursor.execute(create_table_query)
    print("Table `Sailor` created successfully")

    insert_values_query = """
    INSERT INTO Sailor 
    VALUES (%s, %s, %s, %s);
    """
    values_to_insert = [
        (1, 'John Doe', 30, 5),
        (2, 'Jane Smith', 25, 7),
        (3, 'Mike Johnson', 35, 6),
        (4, 'Tom Brown', 45, 8)
    ]

    cursor.executemany(insert_values_query, values_to_insert)
    connection.commit()  
    print("Values inserted successfully")

    update_rating_query = """
    UPDATE Sailor
    SET rating = rating + 1;
    """
    cursor.execute(update_rating_query)
    connection.commit()  
    print("Ratings updated successfully")

    delete_sailors_query = """
    DELETE FROM Sailor
    WHERE age > 40;
    """
    cursor.execute(delete_sailors_query)
    connection.commit() 
    print("Sailors with age > 40 deleted successfully")

    cursor.execute("SELECT * FROM Sailor;")
    result = cursor.fetchall()
    print("Remaining rows:")
    for row in result:
        print(row)

except pymysql.MySQLError as e:
    print(f"Error while connecting to MySQL: {e}")
    connection.rollback() 

finally:
    if connection:
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
