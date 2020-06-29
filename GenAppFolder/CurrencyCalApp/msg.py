def message(name, cur, res):

    MESSAGE = """\
    Hi {},

    Your converted currency in {} is {}{}.

    Thank you,
    Currency Converter App Team.""".format(name, cur, cur, res)
    return MESSAGE

import re
text = "anu.testemail2020+person10@gmail.com"
match = re.search(r'^[a-zA-Z0-9.\-_+]+@[a-zA-Z]+\.com$', text)
if match:
    print("yes")
else:
    print("No")
