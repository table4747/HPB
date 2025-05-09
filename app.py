from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_photos(complex_name, room_name):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT photo_url FROM photos
        WHERE complex_name = ? AND room_name = ?
    """, (complex_name, room_name))
    results = cursor.fetchall()
    conn.close()
    return [row[0] for row in results]

@app.route('/', methods=['GET', 'POST'])
def index():
    photos = []
    if request.method == 'POST':
        complex_name = request.form['complex']
        room_name = request.form['room']
        photos = get_photos(complex_name, room_name)
    return render_template('index.html', photos=photos)

if __name__ == '__main__':
    app.run(debug=True)
