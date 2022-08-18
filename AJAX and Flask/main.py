from flask import Flask , render_template , redirect , request , url_for , jsonify
import random

app = Flask(__name__)
random_number = random.randint(0,100)

@app.route("/update" , methods = ["GET" , "POST"])
def update():
    random_number = random.randint(0 , 100);
    return jsonify("" , render_template("randomPlaceholder.html" , x = random_number))

@app.route('/')
def index():
    return render_template('index.html' , x = random_number)
    

if __name__ == "__main__":
    app.run(debug=True);