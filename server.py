from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Show index page"""

    return render_template('home.html')

PORT = int(os.environ.get("PORT", 5000))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
