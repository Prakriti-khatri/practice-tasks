import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#email credentials
sender_email="prakritikhatri746@gmail.com"
recevier_email="ruman.metahorizon@gmail.com"
password="pqpo cgwx pbsb rwkr"
message=MIMEMultipart()
message["from"]=sender_email
message["to"]=recevier_email
message["subject"]="test email"
body="hello, this is a test email send from python"
message.attach(MIMEMultipart(body,"plain"))
try:
  with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email,password)
        server.sendmail(sender_email,recevier_email,message.as_string())
        print("emeil sent successfully!")
except Exception as e:
    print(f"error:{e}")


#timer
import schedule
import time
def send_notification():
 print("this is your schedule notification!")
schedule.every(10).seconds.do(send_notification)
print("scheduler started.press ctrl+c to stop")
while True:
        schedule.run_pending()
        time.sleep(1)