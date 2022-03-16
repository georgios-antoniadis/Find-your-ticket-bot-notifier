from bs4 import BeautifulSoup
import requests 
import re
import tkinter as tk
import tkinter.messagebox
import email
import smtplib
from email.message import EmailMessage

from send_emails_bot import email_alert

def get_page():
    page = requests.get("https://www.viva.gr/tickets/festival/theater/enigmatikes-parallages/")
    return page

def beautify(page):
    soup = BeautifulSoup(page.content, 'html.parser')

    # print(len(soup.findAll("a", {"class":"eb-button eb-button--soldout"})))

    # print(len(soup.findAll("div",{"class":"col-xs-2"})))

    # dates = soup.findAll("div",{"class":"col-xs-2"})
    # for date in dates:
    #     print(date.get_text())

    # print(len(soup.findAll("div",{"class":"col-xs-5 vertical-align equal-width-buttons"})))

    buttons = soup.findAll("div",{"class":"col-xs-5 vertical-align equal-width-buttons"})

    try_later = "Τα εισιτήρια μόλις εξαντλήθηκαν. Υπάρχουν όμως κρατήσεις που ενδέχεται να λήξουν σε λίγα λεπτά. Παρακαλώ δοκιμάστε ξανά αργότερα"

    for button in buttons:
        if len(re.findall("eb-button eb-button--soldout",str(button))) == 0:
            if len(re.findall(try_later,str(button))) == 0:
                print('yes')
                email_alert("Tickets are available!", "You should go and checkout this https://www.viva.gr/tickets/festival/theater/enigmatikes-parallages/", "g.antoniadis21@gmail.com")

    

if __name__ == "__main__":
    # options = firefoxProfile()
    # driver = online_graber(options)
    page = get_page()   
    beautify(page)