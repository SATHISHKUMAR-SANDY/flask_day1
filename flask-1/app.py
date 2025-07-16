from flask import Flask,render_template,request

app = Flask(__name__)

# @app.route('/')
# def home1():
#     return"sandy home'"

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    print('this is print staement')
    return render_template('index.html')

@app.route('/about')
def about():
    return '<h1>This is about page</h1>'


@app.route('/contact')
def contact():
    return """
<h1>sathishkumar</h1>
<h1>full-stack-developer</h1>
"""

@app.route('/hello')
def message():
    return"<h1>Welcome User</h1>"

@app.route('/user/<username>')
def show_user(username):
    return f"<h2>hello {username} Welecome Your page"


@app.route('/submit', methods=['GET', 'POST']) 
def submit():
    if request.method == 'POST':
        print(" POST method used")
        return "Form submitted using POST!"
    else:
        print("GET method used")
        return "This is a GET request to /submit."
    


@app.route('/html') 
def html_structure():
    return """

 <!DOCTYPE html>
    <html>
    <head>
        <title>My Basic Page</title>
    </head>
    <body>
        <h1 style = color:red > Welcome to Flask!</h1>
        <p>This is a basic HTML page returned from a route.</p>

        <h1>This is a Heading (h1)</h1>
        <p>This is a paragraph. It holds blocks of text.</p>
        <br>
        <p>This is a second paragraph after a line break.</p>
        <hr>
        <p>Above this line is a horizontal rule (hr).</p>
    </body>
    </html>

"""  

if __name__ == '__main__':
    app.run(port=8000,debug=True)