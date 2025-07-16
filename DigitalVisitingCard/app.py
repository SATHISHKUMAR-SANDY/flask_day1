from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/about')
def about():
    return"""

<h1>About Me</h1>
        <p>My name is Sathish Kumar.</p>
        <p>I am a passionate full-stack web developer with experience in Python, Flask, SQL, and frontend technologies.</p>
        <p>I love building web applications, learning new technologies, and solving real-world problems with code.</p>
        <hr>
        <p>Contact: sathish@example.com</p>
"""


@app.route('/skill/<name>')
def skill(name):
    return f" your skill is {name}</h1> "

if __name__ == '__main__':
    app.run(debug=True)