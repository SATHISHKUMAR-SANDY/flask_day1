from flask import Flask


app = Flask(__name__)
@app.route('/preview/<site>')
def preview(site):
    return f"""
    <h1>Preview of {site.title()}.com</h1>
    <p>This is a preview of <strong>{site}.com</strong> website.</p>
    """


if __name__ == '__main__':
    app.run(debug=True)
