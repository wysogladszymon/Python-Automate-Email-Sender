from dotenv import dotenv_values
import os
from email.message import EmailMessage
import ssl
import smtplib


def sendEmail(emailSender, emailPassword, emailReceiver, server, port, fileName):
  with open(fileName, 'r') as file:
    lines = file.readlines()
    subject = lines[0]
    body = lines[1:]
  body = [line.strip() for line in body]
  subject = subject.strip()
  e = EmailMessage()
  e.set_content('\n'.join(body))
  e['Subject'] = subject
  e['From'] = emailSender
  e['To'] = emailReceiver
  
  context = ssl.create_default_context()
  
  with smtplib.SMTP_SSL(server, port,context=context) as smtp:
    smtp.login(emailSender, emailPassword)
    smtp.sendmail(emailSender, emailReceiver, e.as_string())
  
  print("Email sent successfully")

def main():
  config = dotenv_values(".env")
  fileName = "message.txt"
  
  emailSender = config["EMAIL_SENDER"]
  emailPassword = config["EMAIL_PASSWORD"]
  emailReceiver = config["EMAIL_RECEIVER"]
  server = "smtp.gmail.com"
  port = 465
  print("Email is being sent to: ", emailReceiver)
  sendEmail(emailSender, emailPassword, emailReceiver, server, port, fileName)  

if __name__ == "__main__":
  main()