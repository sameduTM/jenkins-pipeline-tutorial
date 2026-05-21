from flask import Flask, request

# initialize flask app
app = Flask(__name__)


@app.route('/')
def index():
    return {'status': 'OK'}, 200


@app.route('/create_user', methods=['POST'])
def create_user():

    return {"status": "user added successfully"}, 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5500)
