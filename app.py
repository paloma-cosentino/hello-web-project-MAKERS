import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
# Request:
# GET /hello?name=David

@app.route('/hello', methods=['GET']) #This is a route block
def hello():
    name = request.args['name'] # The value is 'David'

    # Send back a friendly greeting with the name
    return f"Hello {name}!"

@app.route('/goodbye', methods=['POST'])
def goodbye():
    name = request.form['name'] # The value is 'Alice'

    # Send back a fond farewell with the name
    return f"Goodbye {name}!"

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']
    return f'Thanks {name}, you sent this message: "{message}"'

@app.route('/wave', methods=['GET'])
def wave():
    name = request.args['name']
    return f'I am waving at {name}!'
# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://localhost:5000/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"


# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

