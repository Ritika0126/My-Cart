from Product import *
class checkoutregister:
    def __init__(self):
        self.cost=0
        self.payment=0
        self.cart=[]
        self.inventory=[]
        self.inventory.append(Product(101,"pen",2,1))
        self.inventory.append(Product(102,"bag",9,2))
        self.inventory.append(Product(103,"bread",4,1))



    def scan_item(self,id):
        for i in self.inventory:
            if id == i.id:
                self.cart.append(i)
                self.cost += i.price
                break
        else:
            print("item not found")


    def accept_payment(self,amount):
        self.payment+=amount
        
        


    def print_receipt(self):
        change=self.payment-self.cost
        for e in self.cart:
            print("id:",e.id,"cost:",e.price)
        print("change to b given:"+str(change))
        print("thankyou for shopping")


