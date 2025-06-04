##https://dropmail.me/pt/
import yagmail
import pandas
from news import NewsFeed
from datetime import datetime, timedelta
import time


def send_emails(today, two_days_ago, row):
    news_feed = NewsFeed(row["interest"], two_days_ago, today)
    email = yagmail.SMTP("roldao1990@gmail.com", "lmyz saok rpwq lczq")
    email.send(row["email"],
               f"Your {row["interest"]} news for today",
               f"Hello {row["name"]}\n check this out!\n{news_feed.get()}\n Rodolfo",
               "design.txt")


def take_time():
    global today, two_days_ago
    date = datetime.now()
    today = date.strftime("%Y-%m-%d")
    remove_days = date - timedelta(days=2)
    two_days_ago = remove_days.strftime("%Y-%m-%d")
    return today, two_days_ago


while True:
    if datetime.now().strftime('%H:%M') == "23:24":
        df = pandas.read_excel("people.xlsx")

        for index, row in df.iterrows():
            today, two_days_ago = take_time()
            send_emails(today, two_days_ago, row)
    time.sleep(65)
