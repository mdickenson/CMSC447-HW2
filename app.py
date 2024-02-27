from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# connect to sqlite
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# display users
@app.route('/')
def home():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    users = c.fetchall()
    conn.close()
    return render_template('index.html', users=users)

# add user
@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    id = request.form['id']
    points = request.form['points']
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('INSERT INTO users (name, id, points) VALUES (?, ?, ?)', (name, id, points))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

# search for a user
@app.route('/search_user', methods=['POST'])
def search_user():
    search_term = request.form['search_term']
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE name LIKE ?', ('%' + search_term + '%',))
    users = c.fetchall()
    conn.close()
    return render_template('index.html', users=users)

# delete a user
@app.route('/delete_user/<int:user_id>', methods=['GET'])
def delete_user(user_id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
