from flask import Flask, request
import mysql.connector

# initialize flask app
app = Flask(__name__)

# database connection config
conn = mysql.connector.connect(host="mysql_db", user="root", password="")
cur = conn.cursor()

# create database if it does not exist
cur.execute("CREATE DATABASE IF NOT EXISTS some_db")
cur.execute("use some_db")
cur.execute(
    """CREATE TABLE IF NOT EXISTS some_table(email VARCHAR(50),
        name VARCHAR(25))
    """
)


@app.route('/')
def index():
    cur.execute("SELECT * FROM some_table")

    return [{"name": name, "email": email} for (email, name) in cur]


@app.route('/create_user', methods=['POST'])
def create_user():
    email = request.json.get('email')
    name = request.json.get('name')
    query = "INSERT INTO some_table VALUES(%s, %s)"
    cur.execute(query, (email, name))
    conn.commit()

    return {"status": "user added successfully"}, 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5500)
