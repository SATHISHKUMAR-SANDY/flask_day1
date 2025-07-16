from flask import Flask


app = Flask(__name__)
@app.route('/calc/<op>/<int:num1>/<int:num2>')
def calculator(op, num1, num2):
    if op == "add":
        result = num1 + num2
    elif op == "sub":
        result = num1 - num2
    elif op == "mul":
        result = num1 * num2
    elif op == "div":
        result = "Cannot divide by 0" if num2 == 0 else num1 / num2
    else:
        return "<h2>Invalid Operation</h2>"
    return f"<h2>Result: {result}</h2>"

@app.route('/ops')
def list_ops():
    return "<ul><li>add</li><li>sub</li><li>mul</li><li>div</li></ul>"


if __name__ == '__main__':
    app.run(debug=True)
