
import utils
import argparse
import database

def Main():
    parser = argparse.ArgumentParser(prog='Exchange Rate Calculator', description="Foreign Exchange Rate Software for Currency Conversion: Base is USD")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true", help="Print verbose")
    group.add_argument("-q", "--quiet", action="store_true", help="Print quiet")
    group.add_argument("-e", "--email", action="store_true", help="Send Output to my email")
    group.add_argument("-f", "--file", action="store_true", help="Print Output to a file: Currency Conversion.txt")
    parser.add_argument("-u", "--user", required=True, help="User Login Details")
    parser.add_argument("-a", "--amt", type=int, required=True, help="The amount to convert")
    parser.add_argument("-c", "--cur", required=True, choices=['CAD', 'HKD', 'ISK', 'PHP', 'DKK', 'HUF', 'CZK', 'GBP', 'RON', 'SEK', 'IDR', 'INR', 'BRL', 'RUB', 'HRK', 'JPY', 'THB', 'CHF', 'EUR', 'MYR', 'BGN', 'TRY', 'CNY', 'NOK', 'NZD', 'ZAR', 'USD', 'MXN', 'SGD', 'AUD', 'ILS', 'KRW', 'PLN'], help="The currency code to be converted to")
    args = parser.parse_args()


    if not utils.IsUserExist(args.user):
        print("Unknown User {}".format(args.user))
        return


    if not utils.IsPasswordOk(args.user):
        print("Invalid password attempted 3 times")
        return


    email_add = utils.EmailExist(args.user)
    if not email_add:
        print("Please check your email")
        return

    result = utils.Exchangerate(args.cur, args.amt)
    MESSAGE = """\
    Hi {},

    Your converted currency in {} is {}{}.

    Thank you,
    Currency Converter App Team.""".format(args.user, args.cur, args.cur, result)

    if args.verbose:
        print("Your converted currency in {} is {}{}".format(args.cur, args.cur, result))
    elif args.quiet:
        print("{}{}".format(args.cur, result))
    elif args.email:
        utils.Sendemail(email_add, MESSAGE)
    else:
        if args.file:
            f = open("/home/My_Python_Projects/GenAppFolder/CurrencyCalApp/CurCalOutput.txt", "a")
            f.write(str(result))


if __name__ == '__main__':
    Main()


