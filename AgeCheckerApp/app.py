from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/age/<name>/<year>')

def age(name,year):
    current_year = datetime.now().year
    
    try:
        your_year = int(year)
    except ValueError:
        return "<h1>Enter Valid Year</h1>"
    
    if your_year>=current_year:
        return "<h1>Your year higher or same in current year</h1>"

    age = current_year-your_year
    return f"""
        <h1>Your name is:{name}</h1>
        <h1>Your Age is :{age}</h1>
"""



if __name__ == '__main__':
    app.run(debug=True,port=8000)

