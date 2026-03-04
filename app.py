from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Create database table
def create_table():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

create_table()

@app.route('/')
def home():
    return render_template("register.html")


@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name,email,password) VALUES (?,?,?)",
                (name,email,password))
    conn.commit()
    conn.close()

    return render_template("success.html", name=name)


if __name__ == '__main__':
    app.run(debug=True)