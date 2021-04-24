import re
import requests
from requests_html import HTMLSession
import os


url = "https://master.d2kwfk0n68goxe.amplifyapp.com/"
print("Welcome to GoPhish, choose an option")
userInput = input("Press enter to do a demo, enter any other key to specify a url: ")
if(userInput != ''):
    url = input("Choose an url to scrape emails from: ")
EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

session = HTMLSession()
r = session.get(url)
r.html.render()


print(f"Scraping emails from {url}")
if os.path.exists("emailList.txt"):
  os.remove("emailList.txt")
f = open("emailList.txt", "x")
for re_match in re.finditer(EMAIL_REGEX, r.html.raw_html.decode()):
    f.write(re_match.group())
    f.write("\n")
f.close()