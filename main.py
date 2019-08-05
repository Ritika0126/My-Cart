from Product import *
from checkoutregister import *

c=checkoutregister()
def func():
    b='Y'
    while(True):
        if b=='Y':
            code=int(input("Enter the bar code of item"))
            c.scan_item(code)
            b=str(input("do u want to add another item:"))
        else:
            print("cost:"+str(c.cost))
            amnt=int(input("enter the amount paid by customer"))
            if (amnt<0):
                print("invalid amount")
            else:
                c.accept_payment(amnt)
                if(c.payment>=c.cost):
                    c.print_receipt()
                    break
                else:
                    print("amount to b paid"+str(c.cost-amnt))
                    amnt=int(input("enter the amount paid by customer"))
                    

func()
while(True):
    cus=str(input("is there next customer?"))
    if(cus==str('Y')):
        func()
    else:
         break
