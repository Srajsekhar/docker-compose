from flask import Flask
import os
import mysql.connector

app = Flask(__name__)

@app.route("/")
def hello():
    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host=os.getenv("DATABASE_HOST"),
        user=os.getenv("DATABASE_USER"),
        password=os.getenv("DATABASE_PASSWORD"),
        database="my_database"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE();")
    db_name = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return f"Hello, this is connected to the database: {db_name}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

