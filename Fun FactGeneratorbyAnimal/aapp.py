from flask import Flask


app = Flask(__name__)
fun_facts = {
    "dog": "Dogs can learn over 1000 words!",
    "cat": "Cats sleep for 70% of their lives.",
    "elephant": "Elephants never forget!",
    "dolphin": "Dolphins have names for each other!"
}

@app.route('/fact/<animal>')
def animal_fact(animal):
    fact = fun_facts.get(animal.lower(), "No fact found.")
    return f"<h2>{animal.title()} Fact</h2><p>{fact}</p>"

@app.route('/fact/list')
def list_animals():
    return "<ul>" + "".join(f"<li>{a}</li>" for a in fun_facts.keys()) + "</ul>"


if __name__ == '__main__':
    app.run(debug=True)
