import smtplib


sender = "MarcusSwe8080@gmail.com"
password = "ThisIsThePassword!"

server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()
server.login(sender, password)

message = """
Congratulations! We've successfully created account.
Go to the page: https://www.google.com/search?q=clown
Best Regards ^-^ UwU O_o AWA AWA .<.,
GoPhish Team.
"""

targetEmails = open("emailList")
for email in targetEmails:
    print("sending PHISH to " + str(email))
    server.sendmail(sender, email, message)

