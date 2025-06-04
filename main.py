##https://dropmail.me/pt/
import yagmail
import pandas
from news import NewsFeed
from datetime import datetime, timedelta

date = datetime.now()
today = date.strftime("%Y-%m-%d")
remove_days = date - timedelta(days=2)
two_days_ago = remove_days.strftime("%Y-%m-%d")

df = pandas.read_excel("people.xlsx")

for index, row in df.iterrows():
    news_feed = NewsFeed(row["interest"], two_days_ago, today)
    email = yagmail.SMTP("roldao1990@gmail.com", "lmyz saok rpwq lczq")
    email.send(row["email"],
               f"Your {row["interest"]} news for today",
               f"Hello {row["name"]}\n check this out!\n{news_feed.get()}\n Rodolfo",
               "design.txt")

