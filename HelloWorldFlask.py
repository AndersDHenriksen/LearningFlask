from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world!"

# Run with cli in HelloWorldFlask.py folder:
# > export FLASK_APP=hello.py			# On windows export -> set
# > export FLASK_ENV=development		# Use this to enable debug mode. The server will auto reload on code changes.
# > flask run
