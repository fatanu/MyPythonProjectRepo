import argparse
import requests
import logging
import re
import getpass
import json
import smtplib
from email.mime.text import MIMEText
import ssl

LOG_FORMAT = '%(levelname)s %(asctime)s %(message)s'
logging.basicConfig(filename = "/home/log.txt", level = logging.DEBUG, format = LOG_FORMAT)
logger = logging.getLogger()
def validemail(em):
    match = re.search(r'^[a-zA-Z0-9.\-_+]{6,}@[a-zA-Z]+\.com$', em)
    if match:
      return True
    else:
      print("""Invalid email address format, please enter your valid email associated with your account
                                      Format: min of 6 length and must end with .com""")

def sendemail(email_addy, message):
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "anu.testemail2020@gmail.com"
    receiver_email = email_addy
    password = getpass.getpass(prompt="SMTP Server Password: ")

    msg1 = MIMEText(message)
    msg1['Subject'] = 'Welcome to Currnecy Converter Application '
    msg1['From'] = sender_email
    msg1['To'] = receiver_email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg1.as_string())
        server.quit()

def login(user):
    userd  = {
    1 : {
        "username": "anu",
        "password": "pass1",
        "email": "anu.testemail+person1@gmail.com" # Next work
    },
    2 : {
        "username": "ifedi",
        "password": "pass2",
        "email": "anu.testemail+person2@gmail.com"
    },
    3 : {
        "username": "tise",
        "password": "pass3",
        "email": "anu.testemail+person3@gmail.com"
    },
    4 : {
        "username": "caleb",
        "password": "pass4",
        "email": "anu.testemail+person4@gmail.com"
    },
    5 : {
        "username": "funmi",
        "password": "pass5",
        "email": "anu.testemail+person5@gmail.com"
    },
    6 : {
        "username": "anu1",
        "password": "pass6",
        "email": "anu.testemail+person6@gmail.com"
    },
    7 : {
        "username": "ifedi1",
        "password": "pass7",
        "email": "anu.testemail+person7@gmail.com"
    },
    8 : {
        "username": "tise1",
        "password": "pass8",
        "email": "anu.testemail+person8@gmail.com"
    },
    9 : {
        "username": "caleb1",
        "password": "pass9",
        "email": "anu.testemail+person9@gmail.com"
    },
    10 : {
        "username": "funmi1",
        "password": "pass10",
        "email": "anu.testemail+person10@gmail.com"
    }
    }

    count = 3
    isFound = False
    isUserValid = False
    #user = args.user
    for id, cred in userd.items():
        if cred['username'] == user:
            isUserValid = True
        print("Unknown username")
    if isUserValid:
        while count > 0:
            password = getpass.getpass(prompt= "Password: ")
  # if validateEmail(email):
    #pass
            count -= 1
            for id, cred in userd.items():
                if cred['username'] == user and cred['password']:
                    print('User {} Successfully Logged in to the Currency Converter Application'.format(user))
      #call send email funtion
                    logger.info('user {} logged in successfully to the Currency Converter Application'.format(user))
                    isFound = True
            if isFound:
                break
            if count > 0:
                logger.info('user {} failed to login due to wrong cred, count = {}'.format(username, 3-count))
                print('You now have {} login nattempts left'.format(count))
            else:
                logger.info('user {} Account locked'.format(user))
    #call send email funtion
                print('Account is locked')
    email_add = input("Verify Email Registered with the Account: ")
    if isUserValid:
        message1 = """\
        Hi {},

        You have successfully logged in to Currency Converter Application.

        Thank you,
        Currency Converter App Team.""".format(user)
    validateemail = validemail(email_add)
    emailexist = False
    for id, cred in userd.items():
        if cred['email'] == email_add:
            emailexist = True
    if validateemail:
        sendemail(email_add, message1)

def exchangerate(cur_code, amount):
    val = requests.get("https://api.exchangeratesapi.io/latest", params={"base":"USD"})
    val = json.loads(val.text)
    return amount * val["rates"][cur_code.upper()]


def Main():
    parser = argparse.ArgumentParser(prog='Exchange Rate Calculator', description="Foreign Exchange Rate Software for Currency Conversion: Base is USD")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true", help="Print verbose")
    group.add_argument("-q", "--quiet", action="store_true", help="Print quiet")
    group.add_argument("-e", "--email", action="store_true", help="Send Output to my email")
    group.add_argument("-f", "--file", action="store_true", help="Print Output to a file: Currency Conversion.txt")
    parser.add_argument("-u", "--user", required=True, help="User Login Details")
    parser.add_argument("-a", "--amt", type=int, required=True, help="The amount to convert")
    parser.add_argument("-c", "--cur", required=True, help="The currency code to be converted to")
    args = parser.parse_args()
    login(args.user)
    result = exchangerate(args.cur, args.amt)
    message2 = """\
    Hi {},

    Your converted currency in {} is {}{}.

    Thank you,
    Currency Converter App Team.""".format(args.user, args.cur, args.cur, result)

    if args.verbose:
        print("Your converted currency in {} is {}{}".format(args.cur, args.cur, result))
    elif args.quiet:
        print("{}{}".format(args.cur, result))
    elif args.email:
        sendemail(email_add, message2)
    else:
        if args.file:
            f = open("/home/Cur.txt", "a")
            f.write(str(result))
if __name__ == '__main__':
    Main()
