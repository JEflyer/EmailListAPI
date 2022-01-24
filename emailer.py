import yagmail
import db
import pandas as pd
from data import Email

db.addEmail(Email("jonny","else","testEmail@email.com","number"))

data = pd.DataFrame(db.getEmails(),columns=["id","email"])

yag = yagmail.SMTP("Your Gmail", "Your Application Specific Password")

subject = ""

html_msg = """<p>Hi!<br>
              How are you?<br>
              <img src="https://ipfs.io/ipfs/QmPG9FFHye3NdA4K2XJLqMWbygQF8NqsewhCrSaEJobNnq" width="400" height="200"/>
              Here is the <a href="http://www.python.org">link</a> you wanted.</p>"""


def send(email):
    yag.send(email, subject, html_msg)

for email in data["email"]:
    send(email)

