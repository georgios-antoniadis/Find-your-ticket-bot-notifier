# Find-your-ticket-bot-notifier
# Find-your-ticket-bot This is a web scraping bot designed to get you notified as soon as tickets are available for the show/s you wanna watch!  For this project you will need: - Geckodriver - BeautifulSoup 4  Please be aware that the credentials withing the files have been replaced by placeholders.  In order for the script to run fully automated you will need to add it in your crontab: For Linux: 0) Open a terminal 1) crontab -e 2) At the end of the file add: 15 * * * * &lt;your python directory> &lt;the script directory> &lt;path to your log file> 2>&amp;1