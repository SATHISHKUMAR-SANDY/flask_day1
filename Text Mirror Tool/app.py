from flask import Flask


app = Flask(__name__)

@app.route('/mirror/<text>')
def mirror(text):
    reversed_text = text[::-1]
    length = len(text)
    return f"""
    <h1>Text Mirror</h1>
    <table border='1' cellpadding='10'>
        <tr><th>Original</th><th>Reversed</th><th>Length</th></tr>
        <tr><td>{text}</td><td>{reversed_text}</td><td>{length}</td></tr>
    </table>
    <pre>Original: {text}\nReversed: {reversed_text}</pre>
    """



if __name__ == '__main__':
    app.run(debug=True)
