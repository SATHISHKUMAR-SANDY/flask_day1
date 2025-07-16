from flask import Flask
from datetime import datetime
from zoneinfo import ZoneInfo
import pytz
app = Flask(__name__)


@app.route('/display/<name>')
def display(name):
    return f"<h1>Hello{name}"


@app.route('/greet/<name>')
def greet(name):
    india = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(india).hour
    if current_time<=11:
        return f"<h1>Hello {name} GoodMorning</h1>"
    elif current_time >=12:
        return f"<h1>Hello {name} Good Afternoon"


@app.route('/profile/<username>/<int:age>')

def profile(username,age):
    return f"""<h1>name {username}<h1>
    <h1> Age : {age}"""



if __name__ =='__main__':
    app.run(debug=True)