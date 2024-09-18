from computer import Computer
class ResaleShop:

    # What attributes will it need?
    inventory : list
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []
    # What methods will you need?
    def buy(self, computer):
       if computer not in self.inventory: 
            self.inventory.append(computer)
            print("Bought computer")
       else:
           print("Computer is already in inventory")
           

    def sell(self, computer):
       if computer in self.inventory:
            self.inventory.remove(computer)
       else: 
           print("Computer not in inventory")
           




    def refurbish(self, computer, new_price, new_os):
        if computer in self.inventory:
            computer.update_price(new_price) #calling from computer class
            computer.update_os(new_os)
            print("Computer has been refurbushed. The new price is", computer.price, "and new os is" + computer.os)
        else:
            print("Computer not in inventory")



def main():
    #Make a computer first
    c = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )
    myShop = ResaleShop()
    myShop.buy(c)

main()