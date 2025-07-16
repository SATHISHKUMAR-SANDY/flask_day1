from flask import Flask


app = Flask(__name__)
@app.route('/greet/<int:hour>')
def greet(hour):
    if 5 <= hour < 12:
        greeting = "Good Morning"
    elif 12 <= hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Night"
    return f"<h2>{greeting}!</h2>"

@app.route('/greet/info')
def greet_info():
    return "<p>Use /greet/10 (0-23 format) to get greeting based on hour.</p>"


if __name__ == '__main__':
    app.run(debug=True)
