from os import link
from bs4 import BeautifulSoup
from numpy import number
import requests 
import re

from send_emails_bot import email_alert
from mails_list import mails_list

link_to_play = "https://www.viva.gr/tickets/festival/theater/enigmatikes-parallages/"

def get_page():
    page = requests.get(link_to_play)
    return page

def page_check(page):
    soup = BeautifulSoup(page.content, 'html.parser')

    buttons = soup.findAll("div",{"class":"col-xs-5 vertical-align equal-width-buttons"})

    try_later = "Τα εισιτήρια μόλις εξαντλήθηκαν. Υπάρχουν όμως κρατήσεις που ενδέχεται να λήξουν σε λίγα λεπτά. Παρακαλώ δοκιμάστε ξανά αργότερα"

    tickets_available_flag = False

    number_of_shows = 0

    for button in buttons:
        if len(re.findall("eb-button eb-button--soldout",str(button))) == 0:
            if len(re.findall(try_later,str(button))) == 0:
                tickets_available_flag=True
                number_of_shows += 1
                # print('This is a failsafe check!')

    return tickets_available_flag, number_of_shows

def send_mails(flag,mail,number_of_shows):
    subject="Tickets are available"
    body="You should go and checkout this " + link_to_play + \
         "\n" + "Number of shows: " + str(number_of_shows)
    if flag:
        email_alert(subject, body, mail)


if __name__ == "__main__":
    page = get_page()
    flag, number_of_shows = page_check(page)
    for mail in mails_list:   
        send_mails(flag,mail,number_of_shows)