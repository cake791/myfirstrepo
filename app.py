from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from pathlib import Path

app = Flask(__name__)
DB_PATH = Path('appointments.db')

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS appointments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    email TEXT NOT NULL,
                    appt_date TEXT NOT NULL,
                    appt_time TEXT NOT NULL,
                    service TEXT NOT NULL
                )''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    appt_date = request.form['date']
    appt_time = request.form['time']
    service = request.form['service']

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''INSERT INTO appointments(name, phone, email, appt_date, appt_time, service)
                 VALUES (?, ?, ?, ?, ?, ?)''',
              (name, phone, email, appt_date, appt_time, service))
    conn.commit()
    conn.close()

    return render_template('confirmation.html', name=name, appt_date=appt_date, appt_time=appt_time)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
