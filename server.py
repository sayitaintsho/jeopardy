from flask import Flask
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
def hello():
    clue = get_random_clue()
    return "<h1>Category is {}</h1><h2>Clue is {}<br/><div style='display:none'>{}</div>".format(clue[5], clue[6], clue[7])

if __name__ == "__main__":
    app.run(debug=True)