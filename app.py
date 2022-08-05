from flask import Flask, flash, redirect , render_template, request, session , url_for
# from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer


app = Flask(__name__);
app.secret_key = "samplekeymessageoverhere"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///users.sqlite3';
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False;
# app.permanent_session_lifetime = timedelta(daye = 4);

database = SQLAlchemy(app)

class users(database.Model):
    _id = database.Column("id" , database.Integer , primary_key = True);
    name = database.Column(database.String(200));
    email = database.Column(database.String(200));

    def __init__(self , name , email):
        self.name = name;
        self.email = email;

@app.route('/')
def home():
    return render_template("index.html");

@app.route("/login" , methods = ['POST' , 'GET'])
def login():
    if request.method == "POST":
        # session.permanent = True;
        name = request.form["username"];
        session["user"] = name;

        found_user = users.query.filter_by(name=name).first();
        if found_user:
            session['email'] = found_user.email;
        else:
            user = users(name , "");
            database.session.add(user);
            database.session.commit();

        flash("Login Successful")
        return redirect(url_for("user" , usr=name))
    else:
        if "user" in session:
            flash("Already Logged In")
            return redirect(url_for("user"));
        return render_template("login.html");
        

@app.route("/user" , methods = ["POST" , "GET"])
def user():
    email = None;
    if "user" in session:
        user = session["user"];
            
        if request.method == "POST":
            email = request.form["email"];
            session['email'] = email;
            
            found_user = users.query.filter_by(name=user).first();
            found_user.email = email;
            database.session.commit();

            flash("Emal Updated")
        else:
            if "email" in session:
                email = session['email'];

        return render_template("user.html" , user = user , email = email);
    else:
        flash("You are not logged in")
        return redirect(url_for("login"));

@app.route("/view")
def view():
    return render_template("view.html" , values = users.query.all())

@app.route("/logout")
def logout():
    flash("You have been logged out successfully!")
    session.pop("user" , None);
    session.pop("email" , None);
    return redirect(url_for("login"));

if __name__ == "__main__":
    database.create_all();
    app.run(debug=True);
