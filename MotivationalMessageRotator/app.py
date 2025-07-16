from flask import Flask
import random

app = Flask(__name__)

motivational_quotes = {
    1: "Believe in yourself and all that you are.",
    2: "Your only limit is your mind.",
    3: "Push yourself, because no one else is going to do it for you.",
    4: "Success doesn’t come from what you do occasionally. It comes from what you do consistently.",
    5: "Dream it. Wish it. Do it.",
    6: "Great things never come from comfort zones.",
    7: "Don’t stop when you’re tired. Stop when you’re done.",
    8: "The harder you work for something, the greater you’ll feel when you achieve it.",
    9: "Wake up with determination. Go to bed with satisfaction.",
    10: "Do something today that your future self will thank you for."
}


@app.route('/message')
def message():
    key = random.randint(1,10)
    quote = motivational_quotes.get(key,"No quotes")
    return f"""
        <h1>Today Motivation Qutoe</h1>
        <h3> {quote} </h3>

"""

@app.route('/add/message/<int:index>')
def manual_message(index):
    quote = motivational_quotes.get(index,"No quotes")
    return f"""
        <h1 style = color:red>Today Motivation Qutoe</h1>
        <h3 style = color:blue> {quote} </h3>
"""

if __name__ == ('__main__'):
    app.run(debug=True,port=8000)