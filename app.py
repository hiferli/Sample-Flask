from flask import Flask, flash, redirect , render_template, request, session , url_for
# from datetime import timedelta
import sqlalchemy


app = Flask(__name__);
app.secret_key = "samplekeymessageoverhere"
# app.permanent_session_lifetime = timedelta(daye = 4);

@app.route('/')
def home():
    return render_template("index.html");

@app.route("/login" , methods = ['POST' , 'GET'])
def login():
    if request.method == "POST":
        # session.permanent = True;
        name = request.form["username"];
        session["user"] = name;
        flash("Login Successful")
        return redirect(url_for("user" , usr=name))
    else:
        if "user" in session:
            flash("Already Logged In")
            return redirect(url_for("user"));
        return render_template("login.html");
        

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"];
        return render_template("user.html" , user = user);
    else:
        flash("You are not logged in")
        return redirect(url_for("login"));

@app.route("/logout")
def logout():
    flash("You have been logged out successfully!")
    session.pop("user" , None);
    return redirect(url_for("login"));

if __name__ == "__main__":
    app.run(debug=True);
