from flask import Flask

app = Flask(__name__)

@app.route('/portfolio/<name>')
def portfolio(name):
    return f"""
    <html>
        <head><title>{name.title()}'s Portfolio</title></head>
        <body>
            <h1>Welcome to {name.title()}'s Portfolio</h1>
            <p><strong>Name:</strong> {name.title()}</p>
            <p><strong>Role:</strong> Full Stack Developer</p>
            <p><strong>Email:</strong> {name.lower()}@example.com</p>
            <p><a href="/portfolio/{name}/skills">View Skills</a></p>
            <p><a href="/portfolio/{name}/projects">View Projects</a></p>
        </body>
    </html>
    """


@app.route('/portfolio/<name>/skills')
def skills(name):
    return f"""
    <html>
        <head><title>{name.title()} - Skills</title></head>
        <body>
            <h2>{name.title()}'s Skills</h2>
            <ul>
                <li>Python</li>
                <li>Flask</li>
                <li>HTML & CSS</li>
                <li>JavaScript</li>
                <li>SQL</li>
            </ul>
            <a href="/portfolio/{name}">Back to Profile</a>
        </body>
    </html>
    """

@app.route('/portfolio/<name>/projects')
def projects(name):
    return f"""
    <html>
        <body>
            <h2>{name.title()}'s Projects</h2>
            <table border="1" cellpadding="5">
                <tr>
                    <th>Project Name</th>
                    <th>Description</th>
                    <th>Status</th>
                </tr>
                <tr>
                    <td>Portfolio Website</td>
                    <td>Personal static website using HTML & CSS</td>
                    <td>Completed</td>
                </tr>
                <tr>
                    <td>Flask Blog</td>
                    <td>Dynamic blog using Flask and SQLite</td>
                    <td>Ongoing</td>
                </tr>
                <tr>
                    <td>E-commerce App</td>
                    <td>Flask-based cart and payment system</td>
                    <td>Planned</td>
                </tr>
            </table>
            <br>
            <a href="/portfolio/{name}">← Back to Profile</a>
        </body>
    </html>
    """

if __name__ =='__main__':
    app.run(debug=True)
