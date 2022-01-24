from flask import Flask, request, abort

from db import addEmail,createTable
from data import Email

app = Flask(__name__, static_url_path="/static")


@app.before_request #turn when you need to add mails
def limit_remote_addr():
    if request.remote_addr != "10.20.30.40":
        abort(403)  # Forbidden...


@app.route(
    "/", methods=["GET", "POST"]
)  # take get and post methods both one to render form on frontend post to submit form
def index():
    request_method = request.method
    if request_method == "POST":
        instance = Email(
            request.form[
                "firstName"
            ],  # through request get the values of user input and pass to email instance
            request.form["lastName"],
            request.form["email"],
        )
        try:
            addEmail(instance)  # save in db
            return "success", 200
        except:
            return "error", 500
    

if __name__ == "__main__":
    app.run(debug=True)
