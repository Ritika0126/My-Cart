from Product import *
from checkoutregister import *


def amount_cal(amnt):
    if(amnt<0):
        print("-----invalid amount------")
        amnt=int(input(("please enter valid amount: ")))
        amount_cal(amnt)
    else:
        c.accept_payment(amnt)
        if(c.payment>=c.cost):
            c.print_receipt()
            return
        else:
            print("amount to b paid:  "+str(c.cost-c.payment))
            amnt=int(input("enter the amount paid by customer:  "))
            amount_cal(amnt)
def func():
    #c=checkoutregister()
    b='Y'
    while(True):
        if b=='Y':
            code=int(input("Enter the bar code of item: "))
            c.scan_item(code)
            b=str(input("do u want to add another item: "))
        else:
            print("cost:"+str(c.cost))
            amnt=int(input("enter the amount paid by customer: "))
            amount_cal(amnt)
            break;
                    

#func()
while(True):
    cus=str(input("is there a customer? "))
    if(cus==str('Y')):
        c=checkoutregister()
        func()
    else:
         break
