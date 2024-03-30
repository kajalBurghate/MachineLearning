import os
from sys import *
import smtplib,ssl
import urllib.error
import urllib.request

def is_connected(): # to check internet is connected or not
    try:
        urllib.request.urlopen('http://www.gmail.com')
        return True
    except urllib.error.URLError as err:
        return False

def MailSender(mailid):
    try:
        fromadd = "knagane12792@gmail.com" #from which we send email from that id
        toadd = mailid  #to which mail received id

        Message = """
        Hello %s,
        This is auto generated mail.
        From : - Marvellous Infosystems
        """%(toadd)

        s = smtplib.SMTP('smtp.gmail.com',587) #protocol 587 portnumber

        s.starttls()  #secure connection to establish connection

        s.login(fromadd,"jbkd vqqa uhrs tgsx") #app password which is generated

        s.sendmail(fromadd,toadd,Message) #used to send mail actually

        s.quit() #close connection and vanish content
        
        print("Mail Successfully Send")

    except Exception as E:
        print("Unable to send mail.",E)       

def main():

    if(len(argv) == 2):
        if (argv[1] == "-h") or (argv[1] == "-H"):
            print("This Script is used to send mail")
            exit()

        if (argv[1] == "-u") or (argv[1] == "-U"):
            print("usage : ApplicationName")
            exit()

    try:
        MailSender("burghate.ashish@gmail.com")

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid input",E)

if __name__ == "__main__":
    main()    