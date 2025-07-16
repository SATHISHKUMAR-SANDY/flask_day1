from flask import Flask

app = Flask(__name__)

@app.route('/zodiac/<date>')
def zodiac(date):
    try:
        parts = date.split('-')  # Splits: ['2000', '12', '25']
        if len(parts) != 3:
            return "<h3><i>Invalid format!</i> Please use YYYY-MM-DD</h3>"
        
        year, month, day = parts
        month = int(month)

        # Dummy zodiac logic based on month
        zodiac_signs = {
            1: "Capricorn", 2: "Aquarius", 3: "Pisces", 4: "Aries",
            5: "Taurus", 6: "Gemini", 7: "Cancer", 8: "Leo",
            9: "Virgo", 10: "Libra", 11: "Scorpio", 12: "Sagittarius"
        }

        sign = zodiac_signs.get(month, "Unknown")
        
        return f"""
        <h1>Zodiac Finder</h1>
        <p>Your Date: <strong>{date}</strong></p>
        <hr>
        <p><strong>Your Zodiac Sign:</strong> <i>{sign}</i></p>
        """
    
    except Exception as e:
        return f"<h3>Error: {e}</h3>"

@app.route('/zodiac/help')
def help_page():
    return """
    <h1>Zodiac Sign Help</h1>
    <p>To get your zodiac sign, use this format:</p>
    <strong>/zodiac/YYYY-MM-DD</strong><br><br>
    Example: <i>/zodiac/2000-12-25</i><br>
    <hr>
    <p>This will return your zodiac sign based on the month.</p>
    """

if __name__ == '__main__':
    app.run(debug=True, port=8000)
