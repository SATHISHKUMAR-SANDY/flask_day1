from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return """

<!DOCTYPE html>
    <html>
    <head>
        <title>Banner Page</title>
    </head>
    <body>
        <h1>Enter your banner text</h1>
        <p><a href="/banner/Hello">Click here to view banner: Hello</a> or <a href ="/banner/Hello/32"> Click here to view Large texxt banner </a> </p>
    
    </body>
    </html>

"""



@app.route('/banner/<text>')
def banner_txt(text):
    return f"<h1 style = color:red > Your banner Text is {text}"


@app.route('/banner/<text>/<int:size>')
def large_text(text,size):
    return f"<h1 style =font-size:100px>Your banner Text is {text}</h1>"
    
    
if __name__ =='__main__':
    app.run(debug=True)
