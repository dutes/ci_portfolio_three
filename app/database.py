import sqlite3

def connect_db():
    """
    Connects to the SQLite database and returns the connection object.
    
    Returns:
        sqlite3.Connection: The connection object to the SQLite database.
    """
    return sqlite3.connect('blackjack_game.db')

def create_table():
    """
    Creates the highscores table in the SQLite database if it does not exist.

    This function connects to the database, creates a cursor, and executes an
    SQL statement to create the highscores table.
    If the table already exists, the SQL statement is not executed.
    After executing the SQL statement, the changes are committed and
    the connection to the database is closed.

    Parameters:
        None

    Returns:
        None
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS highscores
                      (id INTEGER PRIMARY KEY, name TEXT, score INTEGER)''')
    conn.commit()
    conn.close()

def add_highscore(name, score):
    """
    Adds a highscore to the highscores table in the SQLite database.
    
    This function connects to the database, creates a cursor, and executes an
    SQL statement to insert a new highscore into the highscores table.
    The SQL statement uses placeholders (?) to prevent SQL injection attacks.
    
    After executing the SQL statement, the changes are committed and
    the connection to the database is closed.
    The function then calls the maintain_highscores function to ensure 
    that only the top 3 highscores are kept in the table.
    
    Parameters:
        name (str): The name of the player.
        score (int): The score achieved by the player.  
        
    Returns:
        None
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO highscores (name, score) VALUES (?, ?)',
                   (name, score))
    conn.commit()
    conn.close()
    maintain_highscores()

def get_highscores():
    """
    Retrieves the top 3 highscores from the highscores table in the SQLite
    database.
    
    This function connects to the database, creates a cursor, and executes
    an SQL statement to select the name and score of the top 3 highscores.
    The SQL statement orders the highscores by score in descending order
    and limits the results to 3 rows.
    
    After executing the SQL statement, the highscores are fetched and
    stored in a variable.
    The connection to the database is then closed.
    
    Parameters:
        None
    
    Returns:
        list of tuples: A list of tuples containing the name and score
        of the top 3 highscores.
    
    Example:
        [('Alice', 100), ('Bob', 90), ('Charlie', 80)]
    
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT name, score FROM highscores ORDER BY score DESC LIMIT 3')
    highscores = cursor.fetchall()
    conn.close()
    return highscores

def get_lowest_highscore():
    """
    Retrieves the lowest highscore from the highscores table in the SQLite
    database.
    
    This function connects to the database, creates a cursor, and executes
    an SQL statement to select the id and score of the lowest highscore.
    The SQL statement orders the highscores by score in ascending order
    and limits the results to 1 row.
    
    After executing the SQL statement, the lowest highscore is fetched
    and stored in a variable.
    The connection to the database is then closed.
    
    Parameters:
        None
        
    Returns:
        tuple: A tuple containing the id and score of the lowest highscore.
        
    Example:
        (1, 50)
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, score FROM highscores ORDER BY score ASC LIMIT 1')
    lowest = cursor.fetchone()
    conn.close()
    return lowest

def delete_highscore(score_id):
    """
    Deletes a highscore from the highscores table in the SQLite database.
    
    This function connects to the database, creates a cursor, and
    executes an SQL statement to delete a highscore from the highscores table.
    The SQL statement uses placeholders (?) to prevent SQL injection attacks.
    
    After executing the SQL statement, the changes are committed
    and the connection to the database is closed.
    
    Parameters:
        score_id (int): The id of the highscore to be deleted.
    
    Returns:
        None
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM highscores WHERE id = ?', (score_id,))
    conn.commit()
    conn.close()

def maintain_highscores():
    """
    Maintains the highscores table by keeping only the top 3 highscores.

    This function connects to the database, creates a cursor, and
    executes an SQL statement to count the number of rows in the
    highscores table.
    If the number of rows is greater than 3, the function calls
    the get_lowest_highscore function to get the lowest highscore.
    The function then calls the delete_highscore function to delete
    the lowest highscore.
    After deleting the lowest highscore, the connection to the
    database is closed.

    Parameters:
        None
    
    Returns:
        None
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM highscores')
    count = cursor.fetchone()[0]
    if count > 3:
        lowest = get_lowest_highscore()
        delete_highscore(lowest[0])
    conn.close()
