import pandas as pd
import datetime
import smtplib
import time
import requests
from win10toast import ToastNotifier
#from ML import data

df = pd.read_excel(r'C:\Users\burgh\Desktop\Python\ML\data.xlsx')

GMAIL_ID = 'knagane12792@gmail.com'
GMAIL_PWD = 'jbkd vqqa uhrs tgsx'

toast = ToastNotifier()

def SendEmail(to, sub, msg):
    gmail_obj = smtplib.SMTP('smtp.gmail.com', 587)

    gmail_obj.starttls()

    gmail_obj.login(GMAIL_ID, GMAIL_PWD)

    gmail_obj.sendmail(GMAIL_ID, to, f"Subject : {sub}\n\n{msg}")

    gmail_obj.quit()

    print("Email sent to " +str(to) + "with subject" +str(sub) +"and message :"+str(msg))

    toast.show_toast("Email Sent!", threaded = True, icon_path = None, duration = 6)

    while toast.notification_active():
        time.sleep(0.1)

if __name__ == "__main__":
    dataframe = pd.read_excel("excelsheet.xlsx")  
    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y")
    writeInd = []                                                  
    for index,item in dataframe.iterrows():
        msg = "Many Many Happy Returns of the day dear " + str(item['NAME'])
        bday = item['Birthday'].strftime("%d-%m")       
        if (today == bday) and yearNow not in str(item['Year']):   
            sendEmail(item['Email'], "Happy Birthday", msg)
            sendsms(item['Contact'], msg, item['NAME'], "Happy Birthday")
            writeInd.append(index)                                 
    for i in writeInd:
        yr = dataframe.loc[i,'Year']
        dataframe.loc[i,'Year'] = str(yr) + ',' + str(yearNow)            
    dataframe.to_excel('excelsheet.xlsx', index = False)






