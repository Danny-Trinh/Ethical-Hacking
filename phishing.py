import smtplib, ssl
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


sender = "MarcusSwe8080@gmail.com"
password = "ThisIsThePassword!"

# server = smtplib.SMTP("smtp.gmail.com", 587)

# server.starttls()
# server.login(sender, password)

####################################################


message = MIMEMultipart("alternative")
message["Subject"] = "Account Compromised"
message["From"] = "Facebook"

# Create the plain-text and HTML version of your message
text = """
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
html = """\
<html>
  <body>
    <img width="140" height="140" src="https://facebookbrand.com/wp-content/uploads/2019/04/f_logo_RGB-Hex-Blue_512.png?w=512&h=512" alt="facebook"></img>
    <p>Warning!<br>
       Your Facebook password has been compromised.
       Click here to update it: 
       <a href="172.16.0.54">Facebook</a> 
       <br>
    </p>
  </body>
</html>
"""

part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")


message.attach(part1)
message.attach(part2)


context = ssl.create_default_context()
targetEmails = open("emailList.txt")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender, password)
    for email in targetEmails:
        print("Phishing " + email)
        try:
            server.sendmail(sender, email, message.as_string())
        except:
            print("email not found" + email + "....")
        




#################################

# email_body = """From: MarcusSwe8080@gmail.com
# To: hi@hi.com
# Subject: Not a fishing email?\n

# Chad sent you 50 lures!
# '<a href="www.google.com">abc</a>'

# """
# message = MIMEText(email_body, 'html')
# targetEmails = open("emailList.txt")

# for email in targetEmails:
#     print("sending PHISH to " + str(email))
#     server.ehlo
#     server.sendmail(sender, email, message)

#################################
