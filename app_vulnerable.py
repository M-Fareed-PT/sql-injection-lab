# app_vulnerable.py
from flask import Flask, request, render_template_string, g
import sqlite3

DB = 'lab.db'
app = Flask(__name__)

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DB)
    return g.db

@app.teardown_appcontext
def close_conn(exc):
    db = g.pop('db', None)
    if db:
        db.close()

LOGIN_HTML = """
<!doctype html>
<title>Vulnerable Login</title>
<h1>Vulnerable Login (Demo)</h1>
<form method="post">
  Username: <input name="username"><br>
  Password: <input name="password"><br>
  <input type="submit" value="Login">
</form>
<p>{{ message }}</p>
"""

@app.route('/', methods=['GET','POST'])
def login():
    msg = ''
    if request.method == 'POST':
        u = request.form.get('username','')
        p = request.form.get('password','')
        # Vulnerable string formatting -> SQL injection possible
        query = f"SELECT id, username FROM users WHERE username = '{u}' AND password = '{p}'"
        db = get_db()
        cur = db.execute(query)
        row = cur.fetchone()
        if row:
            msg = f"Welcome, {row[1]} (id {row[0]})"
        else:
            msg = "Login failed"
    return render_template_string(LOGIN_HTML, message=msg)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
