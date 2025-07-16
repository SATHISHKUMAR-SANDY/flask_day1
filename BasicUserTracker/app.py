from flask import Flask

app = Flask(__name__)


@app.route('/user/<name>')
def user(name):
    print(f"{name} accessed")
    return f"<h1>Welcome {name}</h1>"


@app.route('/user/<name>/city/<city>')
def user_native(name,city):
    print(f"{name},{city} accessed")
    return f"""
<h1>Hiii {name}</h1>
<h1>How is your {city}</h1>
"""
if __name__ == '__main__':
    app.run(debug=True,port=8000)


