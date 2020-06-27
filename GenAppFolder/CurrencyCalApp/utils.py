import requests
import logging
import re
import getpass
import json
import smtplib
from email.mime.text import MIMEText
import ssl
import database
import msg


LOG_FORMAT = '%(levelname)s %(asctime)s %(message)s'
logging.basicConfig(filename = "/Users/bebede/Documents/class2/log", level = logging.DEBUG, format = LOG_FORMAT)
logger = logging.getLogger()


def Validemail(em): #while for 3 times
  if len(em) > 6:
    match = re.search(r'^[a-zA-Z0-9.\-_+]{6,}@[a-zA-Z]+\.com$', em)
    if match:
      return True
    else:
      print("""Invalid email address format, please enter your valid email associated with your account
                                      Format: min of 6 length and must end with .com""")
  else:
    pass

def Exchangerate(cur_code, amount):
    val = requests.get("https://api.exchangeratesapi.io/latest", params={"base":"USD"})
    val = json.loads(val.text)
    return amount * val["rates"][cur_code.upper()]

def Sendemail(email_addy, message):
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "anu.testemail2020@gmail.com"
    receiver_email = email_addy
    logger.info("I just sent an email to {}".format(sender_email))
    print("I just sent an email to {}".format(sender_email))
    #password = getpass.getpass(prompt="SMTP Server Password: ")

    '''
    msg1 = MIMEText(message)
    msg1['Subject'] = 'Welcome to Currnecy Converter Application '
    msg1['From'] = sender_email
    msg1['To'] = receiver_email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg1.as_string())
        server.quit()
    '''

def IsUserExist(username):
    for id, cred in database.userd.items():
        if cred['username'] == username:
            return True 

def IsPasswordOk(username):
    count = 3
    isFound = False

    while count > 0:
        password = getpass.getpass(prompt= "Password: ")
        count -= 1
        for id, cred in database.userd.items():
            if  cred['password'] == password:
                print('User {} Successfully Logged in to the Currency Converter Application'.format(username))
                logger.info('user {} logged in successfully to the Currency Converter Application'.format(username))
                isFound = True
                break
        
        if isFound:
            break

        if count > 0:
            print('count yeee')
            logger.info('user {} password not correct, {} attempt remaining'.format(username, 3-count))

        else:
            logger.info('user {} Account locked'.forma(username))

    if isFound:
        print('yeeee')
        return True

def IsEmailValid(username):
    email_add = input("Verify Email Registered with the Account: ")
        
    validateemail = Validemail(email_add)

    for id, cred in database.userd.items():
        if cred['email'] == email_add and cred['username'] == username:
            return True
