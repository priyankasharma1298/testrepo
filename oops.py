
#                    OBJECT ORIENTED PROGRAMMING

# Fill in the Line class methods to accept coordinates as a pair 
# of tuples and return the slope and distance of the line
class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2
    
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
        
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)  

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line((3,2),(8,10))
print(li.distance())
print(li.slope())



# find volume and surface area of cylinder
class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius
        
    def volume(self):
        #pi r2h
        v=(3.14)*(self.radius**2)*self.height
        return v
    
    def surface_area(self):
        #A=2πrh+2πr2
        a=2*(3.14*self.radius*self.height)+ (2*3.14*self.radius**2)
        return a

c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())



# For this challenge, create a bank account class that has two attributes:

# owner
# balance
# and two methods:

# deposit
# withdraw
# As an added requirement, withdrawals may not exceed the available balance.

# Instantiate your class, make several deposits and withdrawals, 
# and test to make sure the account can't be overdrawn

class account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposit(self,deposited_amt):
        self.balance+=deposited_amt
        print(self.balance,"deposited the amount")
        

    def withdraw(self,withdrw_amt):
        if self.balance>withdrw_amt:
            self.balance-=withdrw_amt
            print(withdrw_amt," has been withdraw")
        else:
            print("invalid")    

       
a1=account('Jose',100)  # balance of a1 =100
a2=account('xyz',300)   # balance of a2 =300

a1.deposit(100)   # deposit + balance= 100+100=200 for a1
print("balance of a1 after deposit of 100 = ",a1.balance)
a2.deposit(200)
print(a2.balance)  # deposit + balance= 200+300=500 for a2

a1.withdraw(50)  # invalid as widthdraw amount> balance
print("total balance of a1 after withdraw of 50 =",a1.balance)






               







 





      
                 