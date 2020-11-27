import requests
import telegram
import os
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

access_token = os.environ["BOT_TOKEN"]
bot = telegram.Bot(token='access_token')
url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20201205&screenratingcode=02'

def job_function():
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    imax = soup.select_one('span.imax')
    if (imax):
        bot.sendMessage(chat_id=845281085, text="예매오픈")
        sched.pause()

sched = BlockingScheduler()
sched.add_job(job_function, 'interval', seconds=3)
sched.start()
