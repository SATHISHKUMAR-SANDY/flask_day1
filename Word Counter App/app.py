from flask import Flask


app = Flask(__name__)

@app.route('/wordcount/<text>')
def word_count(text):
    count = len(text.split())
    return f"""
    <h1 style='color:green;'>Word Count Result</h1>
    <p style='font-size:18px;'>Total Words: <strong>{count}</strong></p>
    """

@app.route('/wordcount/help')
def wordcount_help():
    return """
    <h2>How to use</h2>
    <p>Use this format: <i>/wordcount/your+text+goes+here</i></p>
    """

if __name__ == '__main__':
    app.run(debug=True)