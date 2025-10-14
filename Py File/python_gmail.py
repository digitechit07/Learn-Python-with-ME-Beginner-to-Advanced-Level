import os
import smtplib
message = """From: From Person <surajmkhandagale78@gmail.com>
To: TO Person <surajkhp14@gmail.com>
Subject: SMTP email test

This is my first message.
"""
print("start\n")
smtpObj = smtplib.SMTP('smtp.gmail.com',587)
smtpObj.ehlo()
print("\nfisrt")
smtpObj.starttls()
smtpObj.ehlo()
print("second\n")
# C: HELO client.example.com
smtpObj.login('surajmkhandagale78@gmail.com','ggul czeh aqmb gpfx')
print("Third")
smtpObj.sendmail('surajmkhandagale78@gmail.com','surajkhp14@gmail.com',message)
print("Messge send successfully ...")


# Guide : https://www.youtube.com/watch?v=g_j6ILT-X0k
