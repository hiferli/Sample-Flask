from flask import Flask , jsonify

app = Flask(__name__);

@app.route('/')
def hello_world():
    return "Hello World"

@app.route("/palindrome")
def errorDrome():
    result = {
        "Error" : True,
        "Description" : "Please enter a value"
    }

    return jsonify(result);

@app.route("/palindrome/<string:n>")
def palindrome(n = 1):
    if(n == n[::-1]):
        result = {
            "Number" : int(n),
            "isPalindrome" : True
        }
    else:
        result = {
            "Number" : int(n),
            "isPalindrome" : False
        }

    return jsonify(result);
    
if __name__ == "__main__":
    app.run(debug = True);
