from flask import Flask

# Create a Flask web app
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route('/')
def hello_world():
        return 'Hello, Dosto!'

# Run the app with host='0.0.0.0' and port=5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

