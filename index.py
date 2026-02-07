import bugsnag
from bugsnag.flask import handle_exceptions
import os

# Configure bugsnag
bugsnag.configure(
  api_key=os.getenv("BUGSNAG_API_KEY")
)

# Attach bugsnag to Flask's exception handler
app = Flask(__name__)
handle_exceptions(app)

@app.route("/get")
def get():
    return "Hello, World"

@app.route("/bug")
def get():
    return "/bug"
