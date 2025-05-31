##https://dropmail.me/pt/
import yagmail
import pandas


df = pandas.read_excel("people.xlsx")

for index, row in df.iterrows():
    print(row["email"])
    email = yagmail.SMTP("roldao1990@gmail.com", "lmyz saok rpwq lczq")
    email.send(row["email"],
               f"Your {row["interest"]} news for today",
               f"Hello {row["name"]}\n check this out!\n Rodolfo",
               "design.txt")
