import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

# Function to connect to the database
def get_db_connection():
    # This opens the file you created with init_db.py
    conn = sqlite3.connect('database.db')
    
    # This line is CRITICAL: It allows us to access columns by name 
    # (like post['title']) instead of just numbers (like post[0]).
    conn.row_factory = sqlite3.Row 
    return conn

@app.route('/<int:post_id>')
def post(post_id):
    conn = get_db_connection()
    # Fetch only the one post that matches the ID from the URL
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    
    # If the ID doesn't exist, Flask will show an error automatically
    return render_template('post.html', post=post)

@app.route('/')
def index():
    # 1. Open the connection
    conn = get_db_connection()
    
    # 2. Ask the database for all rows in the 'posts' table
    posts = conn.execute('SELECT * FROM posts').fetchall()
    
    # 3. Close the connection (don't leave the door open!)
    conn.close()
    
    # 4. Send the data to the HTML file (which we will create next)
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)