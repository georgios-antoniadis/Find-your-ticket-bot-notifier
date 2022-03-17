# Find-your-ticket-bot-notifier
Find-your-ticket-bot-notifier is a web scraping bot designed to get you notified as soon as tickets are available for the show/s you wanna watch!  

For this project you will need: 
- Geckodriver 
- BeautifulSoup 4  

Please be aware that the credentials withing the files have been replaced by placeholders. In order to work for your situation you must create a new scirpt named creds.py or equivalent and store your information in there. Please be aware that you will be storing your credentials in plain text format on your local machine, which is not advised. It is recommended that you make use of a dummy email address and not your main one.

In order for the script to run fully automated you will need to add it in your crontab: For Linux: 
0) Open a terminal 
1) crontab -e 
2) At the end of the file add: 15 * * * * [YOUR PYTHON'S PATH] [THE SCRIPT'S PATH] [PATH TO YOUR LOG FILE]> 2>&amp;1
3) Go to the parent directory of where your script is stored and open a terminal window
4) Type "cmhod 775 [NAME OF YOUR DIRECTORY]"
