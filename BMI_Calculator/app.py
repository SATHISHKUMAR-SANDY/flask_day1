from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/show')
def show():
    return " <h1>This App Use to Calculate our Body Bmi </h1>"


@app.route('/bmi/<float:height>/<float:weight>')
def bmi(height,weight):
    height_m = height/100
    bmi = round(weight/(height_m**2),2)

    if bmi < 18.5:
        status = "Underweight"
    elif bmi < 24.9:
        status = "Normal weight"
    elif bmi < 29.9:
        status = "Overweight"
    else:
        status = "Obese"

    return f"<h1>Your BMI is: {bmi} — {status}</h1>"



if __name__ == '__main__':
    app.run(debug=True,port=8000)

