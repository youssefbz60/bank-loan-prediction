
"""
Flask application entry point.
The prediction interface will be implemented later.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Bank Loan Prediction Application"


if __name__ == "__main__":
    app.run(debug=True)
