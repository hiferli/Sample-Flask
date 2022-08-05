from flask import render_template , Blueprint

homePage = Blueprint("homePage" , __name__ , static_folder="Static" , template_folder="Templates")

@homePage.route("/")
@homePage.route("/home")
def home():
    return render_template("index.html")