import psycopg2
from itertools import permutations

def insert_row(cursor, new_row_data):
    insert_query = """
    INSERT INTO process_order (userid, p_order)
    VALUES (%(userid)s, %(p_order)s);
    """

    # Execute the query with the data
    cursor.execute(insert_query, new_row_data)

    # Commit the changes to the database
    connection.commit()
    print("Row inserted successfully.")

def remove_row(cursor, userid):
    # Construct and execute the DELETE query
    delete_query = """
    DELETE FROM process_order
    WHERE userid = %(userid)s;
    """
    cursor.execute(delete_query, {'userid': userid})
    # Commit the transaction
    connection.commit()
    print(f"Row with userid {userid} deleted successfully.")




    # Connection parameters
db_params = {
        'host': 'localhost',     # Change this if your database is on a different host
        'port': '5432',          # Default PostgreSQL port
        'database': 'baxter',    # Your database name
        'user': 'postgres', # Your database username
        'password': '1515'  # Your database password
}

try:
    # Establish a connection to the database
    connection = psycopg2.connect(**db_params)
    
    # Create a cursor object to interact with the database
    cursor = connection.cursor()
    confirmation_methods = ["visual","verbal","body","no_confirm"]
    all_orders = list(permutations(confirmation_methods))
    print(all_orders)
    print(len(all_orders))
    for i in range (0,2):
        for j in range(0,len(all_orders)):
            participant_num = i * len(all_orders) + j
            participant_id = "p"+ str(participant_num +1)
            print(participant_id)
            order_data = { "userid": participant_id, "p_order":all_orders[j] }
            insert_row(cursor,order_data)

except (Exception, psycopg2.Error) as error:
    print(f"Error: {error}")

finally:
     # Close the cursor and connection
    if connection:
        cursor.close()
        connection.close()
        print("Connection closed.")




