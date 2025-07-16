from flask import Flask
from datetime import datetime
app = Flask(__name__)

daily_quotes = {
    "monday":    "Start your week with energy and focus!",
    "tuesday":   "Keep going. You’re doing great!",
    "wednesday": "Halfway there – stay strong!",
    "thursday":  "Push through. The weekend is near!",
    "friday":    "Finish strong. You've got this!",
    "saturday":  "Rest, recharge, and smile!",
    "sunday":    "Plan, reflect, and get ready to shine!"
}



@app.route('/show')
def today_quote():
    return"""
<ul>
  <li>"The best way to get started is to quit talking and begin doing." – Walt Disney</li>
  <li>"Success is not final, failure is not fatal: It is the courage to continue that counts." – Winston Churchill</li>
  <li>"Don't watch the clock; do what it does. Keep going." – Sam Levenson</li>
  <li>"Opportunities don't happen. You create them." – Chris Grosser</li>
  <li>"Push yourself, because no one else is going to do it for you." – Unknown</li>
  <li>"Great things never come from comfort zones." – Unknown</li>
  <li>"Dream it. Wish it. Do it." – Unknown</li>
</ul>
"""


@app.route('/quote/<day>')
def day_quote(day):

    day  =day.lower()
    message = daily_quotes.get(day,"No Quote for the day")
    return  f"<h1 style = color:red >{message}</h1>"


if __name__ == '__main__':
    app.run(debug=True)