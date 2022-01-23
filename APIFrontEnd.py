from flask import Flask,abort, request
from db import addEmail
from data import Email

app = Flask(__name__, static_url_path='/static')


@app.before_request
def limit_remote_addr():
  if request.remote_addr != '10.20.30.40':
    abort(403) # Forbidden...

@app.route("/AddEmail/<firstName>/<lastName>/<email>/<number>", methods=['POST'])
def generate(firstName,lastName,email,number):
    if request.method == "POST":
        instance = Email(firstName,lastName,email,number)
        try:
            addEmail(instance)
            return "success", 200
        except:
            return "error",500


if __name__ == "__main__":
    app.run(debug=True)