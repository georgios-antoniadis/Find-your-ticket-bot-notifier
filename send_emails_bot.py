import email
import smtplib
from email.message import EmailMessage

from creds import user, app_pass

def email_alert(subject,body,to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    msg['from'] = user

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user, app_pass)
    server.send_message(msg)

    server.quit()


if __name__ == '__main__':
    num_of_shows = 4
    link_to_play = "https://www.viva.gr/tickets/festival/theater/enigmatikes-parallages/"
    subject="Tickets are available"
    body="You should go and checkout this " + link_to_play + \
        "\n" + "Number of shows: " + str(num_of_shows)
    email_alert(subject, body, "g.antoniadis21@gmail.com")
    # email_alert("hi", "This is a test message", "g.antoniadis21@gmail.com")