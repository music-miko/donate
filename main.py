from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Route for the main donation page
@app.route('/')
def home():
    return render_template('index.html')

# --- Future Expansion Examples Below ---

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/commands')
# def commands():
#     return render_template('commands.html')

# This is only used when running locally, not on Vercel
if __name__ == '__main__':
    app.run(debug=True)
