from flask import Flask, jsonify , redirect , url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World"


@app.route("/palindrome")
@app.route("/palindrome/")
def errorDrome():
    result = {
        "Error": True,
        "Description": "Please enter a value"
    }

    return jsonify(result)

@app.route("/palindrome/<string:n>")
def palindrome(n):
    if (n != None):
        if (n == n[::-1]):
            result = {
                "Number": int(n),
                "isPalindrome": True
            }   
        else:
            result = {
                "Number": int(n),
                "isPalindrome": False
            }
    else :
        return redirect(url_for("errorDrome"));


    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
