import requests
import time
from pprint import pprint
import imaplib


class ExcelFile:
    def __init__(self, filepath):
        self.filepath = filepath

    def get_data(self):
        pass


class Email:
    def __init__(self):
        pass
        # #, sender, receiver, subject, body
        # self.sender = sender
        # self.receiver = receiver
        # self.subject = subject
        # self.body = body

    def send(self):
        pass


class NewsFeed:
    """Representing multiple news titles and links as a single string"""
    API_KEY = "&apiKey=b7c81e35e1c942ee831f80be029826b0"
    URL_BASE = "https://newsapi.org/v2/everything?"
    RAW_URL_HEADLINES = "https://newsapi.org/v2/top-headlines?country=us"
    RAW_URL_SOURCE = "https://newsapi.org/v2/top-headlines?sources=bbc-news"
    RAW_URL_TOPIC = ("https://newsapi.org/v2/everything?"
                     "q=coimbra&"
                     "from=2025-05-28&"
                     "language=pt&"
                     "to=2025-05-29")

    def __init__(self, interest, from_date, to_date, language='en'):
        self.email_body = ""
        self.interest = f"q={interest}&"
        self.from_date = f"from={from_date}&"
        self.to_date = f"to={to_date}"
        self.language = f"language={language}&"

    def _prepare_body(self, dictionary_of_news):
        for line in dictionary_of_news:
            if line["title"] and line["url"]:
                self.email_body += line["title"] + "\n" + line["url"] + "\n\n"
        return self.email_body

    def _get_article(self, url):
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Erro na requisição: {response.status_code} - {response.text}")
        content = response.json()["articles"]
        return content

    def get(self):
        url = self.URL_BASE + self.interest + self.from_date + self.language + self.to_date + self.API_KEY
        content = self._get_article(url)
        body = self._prepare_body(content)
        return body


if __name__ == "__main__":
    news = NewsFeed("coimbra", "2025-05-28", "2025-05-30", "pt")
    print(news.get())
