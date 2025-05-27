class ExcelFile:
    def __init__(self, filepath):
        self.filepath = filepath

    def get_data(self):
        pass


class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body

    def send(self):
        pass


class NewsFeed:
    def __init__(self, data):
        self.data = data

    def get(self):
        pass
