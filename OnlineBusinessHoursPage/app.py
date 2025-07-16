from flask import Flask
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def status():

    current_hour = datetime.now().hour
    
    if current_hour>=9  and current_hour<18:
        return"<h1>We ARE OPEN!</h1>"
    else:
        return "<h1>We are closed!</h1>"

@app.route('/contact')
def contact():
    return """

    <!DOCTYPE html>
    <html>
    <head>
        <title>Contact Page</title>
    </head>
    <body>
        <h1>Contact Me</h1>
        <p><strong>Email:</strong> sathish@example.com</p>
        <p><strong>Phone:</strong> +91-9876543210</p>
    </body>
    </html>

"""


@app.route('/formatting')
def inline_formatting():
    return"""

 <!DOCTYPE html>
    <html>
    <head>
        <title>Inline Formatting</title>
    </head>
    <body>
        <h1>Inline HTML Formatting Example</h1>

        <p>This is a <b>bold</b> word inside a paragraph.</p>
        <p>This is an <i>italic</i> word inside a paragraph.</p>
        <p>This is an <u>underlined</u> word inside a paragraph.</p>

        <hr>

        <p>Combining <b>bold</b>, <i>italic</i>, and <u>underline</u> in one line.</p>

        <p>Line break here<br>Now this appears on a new line.</p>

        <hr>

        <p><b><i><u>Stylish ending!</u></i></b></p>
    </body>
    </html>
"""

if __name__ == '__main__':
    app.run(debug=True)