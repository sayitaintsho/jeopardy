from flask import Flask
from flask import render_template

import sqlite3

app = Flask(__name__)

query = """
SELECT clues.id, clues.game, airdate, round, value, category, clue, answer
FROM clues
JOIN airdates ON clues.game = airdates.game
JOIN documents ON clues.id = documents.id
JOIN classifications ON clues.id = classifications.clue_id
JOIN categories ON classifications.category_id = categories.id
ORDER BY random()
LIMIT 1;"""

def get_random_clue():
    conn = sqlite3.connect('clues.db')
    c = conn.cursor()
    d = c.execute(query)
    return d.fetchone()

@app.route("/")
def index():
    clue = get_random_clue()
    return render_template('jeop.html', category=clue[5], clue=clue[6], answer=clue[7])

if __name__ == "__main__":
    app.run(debug=True)