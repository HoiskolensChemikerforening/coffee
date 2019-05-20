import os
import smtplib
import imghdr
from email.message import EmailMessage

from params import EMAIL_ADDRESS 
from params import EMAIL_PASSWORD 
import datetime

def send_mail(e):
    contacts = ['webkom@hc.ntnu.no']

    msg = EmailMessage()
    msg['Subject'] = 'En feil har skjedd med kaffeknappen'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = 'webkom@hc.ntnu.no'

    msg.set_content('Error')
    date = str(datetime.datetime.now())
    
    msg.add_alternative("""\
    <!DOCTYPE html>
    <html>
        <body>
            <h4>Raspberry pi har sluttet å fungere</h4>
            <h5>Avsluttet: {} </h5>
            <p>
            Feil melding: {} 
            </p>
        </body>
    </html>
    """.format(date, e), subtype='html')


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print("E-post sendt")

if __name__ == "__main__":
    send_mail("Dette er en testmail fra raspberry PIen")
