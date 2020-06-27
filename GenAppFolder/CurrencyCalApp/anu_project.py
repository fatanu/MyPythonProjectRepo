
import utils
import argparse
import database
# import test.test as t
      
    
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

    
    if not utils.IsUserExist(args.user):
        print("Unknown User {}".format(args.user))
        return
    
    
    if not utils.IsPasswordOk(args.user):
        print("Invalid password attempted 3 times")
        return


    if not utils.IsEmailValid(args.user):
        print("Please check your email")
        return

    result = utils.Exchangerate(args.cur, args.amt)
    
    if args.verbose:
        print("Your converted currency in {} is {}{}".format(args.cur, args.cur, result))
    elif args.quiet:
        print("{}{}".format(args.cur, result))
    elif args.email:
        util.Sendemail(email_add, msg.MESSAGE_1)
    else:
        if args.file:
            f = open("/home/Cur.txt", "a")
            f.write(str(result))


if __name__ == '__main__':
    Main()
    

