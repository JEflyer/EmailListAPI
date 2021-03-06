from tkinter.tix import Tree
from flask import Flask, render_template, request, abort
from importlib_metadata import method_cache

from db import addEmail
from data import Email

app = Flask(__name__, static_url_path="/static")


# @app.before_request //turn when you need to add mails
# def limit_remote_addr():
#     if request.remote_addr != "10.20.30.40":
#         abort(403)  # Forbidden...


@app.route(
    "/", methods=["GET", "POST"]
)  # take get and post methods both one to render form on frontend post to submit form
def index():
    request_method = request.method
    if request.method == "POST":
        instance = Email(
            request.form[
                "firstName"
            ],  # through request get the values of user input and pass to email instance
            request.form["lastName"],
            request.form["email"],
            request.form["number"],
        )
        try:
            addEmail(instance)  # save in db
            return "success", 200
        except:
            return "error", 500
    return render_template("Hello.html", request_method=request_method)  # render page


if __name__ == "__main__":
    app.run(debug=True)
