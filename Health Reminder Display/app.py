from flask import Flask


app = Flask(__name__)

@app.route('/reminder/<int:hour>')
def reminder(hour):
    msg = "Time to drink water!" if hour % 3 == 0 else "Stretch your body!"
    return f"<h2>{msg}</h2>"

@app.route('/reminder/help')
def reminder_help():
    return "<p>Use /reminder/13 to get advice for that hour (0-23).</p>"



if __name__ == '__main__':
    app.run(debug=True)
