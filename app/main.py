from flask import Flask
import os
import logging

# Initialize the Flask application
app = Flask(__name__)

# Set up basic logging
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    """Home route returning a welcome message."""
    app.logger.info("Home route accessed")
    return "Hello, DevSecOps!"

if __name__ == "__main__":
    # Use environment variables or default to port 5001
    port = int(os.getenv("PORT", 5001))
    app.run(host="0.0.0.0", port=port)
