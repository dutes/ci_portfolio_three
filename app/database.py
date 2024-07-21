import sqlite3

def connect_db():
    return sqlite3.connect('blackjack_game.db')

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS highscores
                      (id INTEGER PRIMARY KEY, name TEXT, score INTEGER)''')
    conn.commit()
    conn.close()

def add_highscore(name, score):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO highscores (name, score) VALUES (?, ?)', (name, score))
    conn.commit()
    conn.close()
    maintain_highscores()

def get_highscores():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT name, score FROM highscores ORDER BY score DESC LIMIT 3')
    highscores = cursor.fetchall()
    conn.close()
    return highscores

def get_lowest_highscore():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, score FROM highscores ORDER BY score ASC LIMIT 1')
    lowest = cursor.fetchone()
    conn.close()
    return lowest

def delete_highscore(score_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM highscores WHERE id = ?', (score_id,))
    conn.commit()
    conn.close()

def maintain_highscores():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM highscores')
    count = cursor.fetchone()[0]
    if count > 3:
        lowest = get_lowest_highscore()
        delete_highscore(lowest[0])
    conn.close()

def delete_highscores():
    conn = connect_db()
    cursor=conn.cursor()
    cursor=conn.execute('DELETE FROM highscores')
    conn.commit()
    conn.close()
