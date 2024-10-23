import os
from abc import ABC, abstractmethod        
class Login:
    username=''
    def __init__(self):
        print('WELCOME TO  HALYMERS ONLINE STORE')
        print('1)Log in as Admin \n2)Log in as user\n(press 1 for admin and 2 for user)')
        self.Who=input('Enter: ')
        if self.Who=='2':
            print('1)Login\n2)Signup\n(press 1 for Login and 2 for SignUp)')
            self.a=input('Enter: ')
            if self.a=='1':
                self.user_Login()
                Customer()
            elif self.a=='2':
                self.Sign_Up()
                Customer()
            else:
                print('Please type 1 or 2')
                self.__init__()
        elif self.Who=='1':
            Admin()
        else:
            print('Please type 1 or 2')
            self.__init__()

    def user_Login(self):
            print('Hello Customer!')
            Login.username=input('Enter your Username: ')
            self.Password=input('Enter Password: ')
            list_files=os.listdir()
            if (Login.username+'.txt') in list_files:
                f=open(Login.username+'.txt','r')
                verify=f.read().splitlines()
                if self.Password in verify:
                    print('Successfully logged in')
                    print()
                else:
                    print('Incorrect Password')
                    self.user_Login()
            else:
                print('User not found')
                self.Sign_Up()
                
    def Sign_Up(self):
            print('Welcome dear new customer \nSign Up your account please.')
            self.Email=input('Enter your Email: ')
            self.Password=input('Enter Password: ')
            Login.username=input('Enter your username: ')
            file=open(Login.username+'.txt','w')
            file.write(self.Email+'\n')
            file.write(self.Password+'\n')
            file.write(Login.username+'\n')

    

class Files:
    
    def openfile1():
        strg='   Name                       Price                             Specifications'
        
        f=open('utensils.txt','r')
        record=f.readlines()
        for i in record:
            i=i.strip()
            record=i.split(',')
            strg+=f'\n{record[0]:30}{record[1]:30}{record[2]:30}'
        print (strg)

    def openfile2():
        strg='   Name                       Price                             Specifications'
        f=open('Home Appliances.txt','r')
        record=f.readlines()
        for i in record:
            i=i.strip()
            record=i.split(',')
            strg+=f'\n{record[0]:30}{record[1]:30}{record[2]:30}'
        print (strg)

class Exit:
    def __init__(self):
        print('Thank You for shopping Mr/Mrs.',Login.username)
        print('You can avail following features')
        print('1)Feedback (Honest reviews would be highly appreciated )\n2)View Purchase History\n3)Exit')
        enter=input('Enter option number. : ')
        if enter =='1':
            self.Feedback()
        elif enter=='2':
            self.Purchase_History()
        elif enter=='3':
            print('Thank you for shopping from HALYMERS ONLINE STORE')

    def Feedback(self):
        self.review=input('Please give us your valuable review: ')
        print('Thank you for your feedback.Hope to see you again!')

    def Purchase_History(self):
        self.strg='   Name                       Price                Bill'             
        self.f=open(Login.username+'.txt','r')
        self.record=self.f.readlines()
        self.record=self.record[3:]
        for i in self.record:
            i=i.strip()
            self.record=i.split(',')
            self.strg+=f'\n{self.record[0]:30}{self.record[1]:30}{self.record[2]:30}'
        print(self.strg)

        
#here we are making an abstract class to enhance our program
class abstract(ABC):
    @abstractmethod
    def CheckOut():
        pass
    
#
class Customer(abstract,Files,Exit):
    
    cart_item=[]
    item_quantity=[]
    lst=[]
    Bill=0
            
    def __init__(self):  
        print('INSTRUCTIONS!!!\nFollow the guidelines to avoid any hurdle while shopping:\n1)Write the exact product name as shown.\n2)Type Exit to access another category.\n3)You would be able to remove items in the end.\n4)At the end, you will be having your bill.\n*********************************************************')
        print()
        print('    MAIN MENU     ')
        print('*'*25)
        print('Choose the category Mr.',Login.username,sep='')
        print('*'*25)
        print('1)utensils\n2)Home Appliances\n3)Exit')
        self.a=input('Enter category number or press 3 to exit from the shop:')
        print()
        if self.a=='1':
            Files.openfile1()
            self.dict={'Cutlery':40000,'Chopper':800,'Bottle':250,'Brush':100,'Juicer':2500,'Mincer':450,'Basket':1200,'Spoon':200,'Beater':300}
            self.add_cart()
        
        elif self.a=='2':
            Files.openfile2()
            self.dict={'Jwellery Organizer':5000,'Lamp Sticker':800,'Sillicone Hook':100,'Beard Straightener':800,'Perfume optimize refill':400,'Shoe storer':2000,'Soap holder':200}
            self.add_cart()

        elif self.a=='3':
            self.callExit()

    def add_cart(self):
       while True: 
         try:
                Bill=0
                self.add_item=input('Enter the name of item: ')
                print(f'Enter the quantity of {self.add_item}: ',end='')
                self.quantity=input()
                Bill+=self.dict[self.add_item]*int(self.quantity)
                self.cart_item.append(self.add_item)
                self.item_quantity.append(self.quantity)
                self.lst.append([self.add_item,self.quantity,Bill])
                Bill=0
                loopbreak=input('Press e to exit from shop and press y to continue shopping')
                if loopbreak=='e':
                  break
         except:
                print('Please enter the exact product\'s name as shown')
       self.show_cart()   
    
            
    def show_cart(self):
            strg='Name             Quantity              Price'
            for i in self.lst:
                strg+=f'\n{i[0]:20}{i[1]:10}{i[2]:10}'
            print(strg)
            self.Remove_from_cart()
    def Remove_from_cart(self):
        print('Name the item you want to remove\n Or press y to continue to billing: ',end='\n')
        self.remove=input()
        if self.remove=='y' or self.remove=='Y':
            self.f=open(Login.username+'.txt','a')
            for i in self.lst:
                self.f.write(i[0]+',')
                self.f.write(i[1]+',')
                self.f.write(str(i[2])+'\n')
            self.f.close()
            self.CheckOut()
        else:
            for i in self.lst:
                if i[0]==(self.remove):
                    self.remove_quantity=int(input('Enter quantity to be removed: '))
                    if int(i[1])==(self.remove_quantity):
                        self.lst.remove(i)
                        if len(self.lst)==0:
                            print('Your cart is empty')
                            break
                        
                        else:  
                            self.f=open(Login.username+'.txt','a')
                            
                            for i in self.lst:
                                self.f.write(i[0]+',')
                                self.f.write(str(i[1])+',')
                                self.f.write(str(i[2])+'\n')
                            self.f.close()
                            self.CheckOut()
                    elif int(i[1])>(self.remove_quantity):
                        i[1]=int(i[1])
                        i[1]-=self.remove_quantity
                        i[2]=int(i[2])
                        i[2]=(i[2]-(self.dict[self.remove]*int(self.remove_quantity)))
                        self.f=open(Login.username+'.txt','a')
                        for i in self.lst:
                            self.f.write(i[0]+',')
                            self.f.write(str(i[1])+',')
                            self.f.write(str(i[2])+'\n')
                        self.f.close()
                        self.CheckOut()
                    else:
                        print('The quantity in your cart is:',self.quantity)
                        self.Remove_from_cart()
                else:
                  print('This item is not present in your cart\nHeading towards billing')
                  self.CheckOut()              
    def CheckOut(self):
        strg='Name             Quantity              Price'
        for i in self.lst:
            strg+=f'\n{i[0]:20}{i[1]:10}{i[2]:10}'
        print(strg)
        self.callExit()
    def callExit(self):
        Exit()


class Inventory:
    def __init__(self):
        print('Choose category\n1)utensils\n2)Home Appliances')
        self.choose=input('Enter option number: ')
        if self.choose=='1':
            Files.openfile1()

        elif self.choose=='2':
            Files.openfile2()

    def append(file):
        Item=input('Enter name of Item:')
        Price=input('Enter Price: ')
        specifications=input('Enter details about the product: ')
        merge=(Item+','+Price+','+specifications)
        f=open(file,'a')
        f.write(merge)
        f.write('\n')
        f.seek(0)
        f.close()
        print(Item,' is added from the Inventory')
    def Add_Item(self):
        print('Choose category\n1)utensils\n2)Home Appliances')
        self.choose=input('Enter option number: ')
        if self.choose=='1':
            Inventory.append('utensils.txt')

        elif self.choose=='2':
            Inventory.append('Home Appliances.txt')

    def delete(file):
        Lst=[]
        delete_Item=input('Enter the name of item you want to delete: ')
        f=open(file,'r')
        record=f.readlines()
        for i in record:
            i=i.strip()
            record=i.split(',')
            Lst.append(record)
        f.close()
        for i in Lst:
            if i[0] == delete_Item:
               Lst.remove(i)
        f=open(file,'w')
        for i in Lst:
            f.write(i[0]+',')
            f.write(i[1]+',')
            f.write(i[2]+'\n')
        f.close()
        print(delete_Item,' is deleted from the Inventory')
    def Remove_Item(self):
        print('Choose category\n1)utensils\n2)Home Appliances')
        self.choose=input('Enter option number: ')
        if self.choose=='1':
            Inventory.delete('utensils.txt')
        elif self.choose=='2':
            Inventory.delete('Home Appliances.txt')

    def Edit_Inventory(self):
        print('Choose category\n1)Kitchen.\n2)Home')
        self.choose=input('Enter option number: ')
        if self.choose=='1':
            Inventory.Edit('utensils.txt')
        elif self.choose=='2':
            Inventory.Edit('Home Appliances.txt')

    def Edit(file):
        Lst=[]
        edit_Item=input('Enter the name of item which you want to edit: ')
        edit_Price=input('Enter new price of the product: ')
        edit_Details=input('Enter new details about the product: ')
        f=open(file,'r')
        record=f.readlines()
        for i in record:
            i=i.strip()
            record=i.split(',')
            Lst.append(record)
        f.close()
        for i in Lst:
            if i[0] == edit_Item:
               i[1]=edit_Price
               i[2]=edit_Details
        f=open(file,'w')
        for i in Lst:
            f.write(i[0]+',')
            f.write(i[1]+',')
            f.write(i[2]+'\n')
        f.close()


class Admin(Inventory):
    def __init__(self):
        self.AdminEmail=input('Enter your email: ')
        self.AdminPassword=input('Enter Password: ')
        if self.AdminEmail=='doaahmed891@gmail.com' and self.AdminPassword=='hello123':
            print('Welcome Administrator')
            while True:
                print('*************************************')
                print('MAIN MENU')
                print('1)Show Inventory.\n2)Add Item.\n3)Remove Item.\n4)Edit_Inventory.\n5)Customer Records \n6)Exit')
                a=input('Enter operation number: ')
                if a=='1':
                    Inventory.__init__(self)
                elif a=='2':
                    Inventory.Add_Item(self)
                elif a=='3':
                    Inventory.Remove_Item(self)
                elif a=='4':
                    Inventory.Edit_Inventory(self)
                elif a=='5':
                    self.Customer_Record()
                elif a=='6':
                    print('You are successfully logged out from admin account')
                    break
                    
        else:
           print('Please enter correct credentials')

    def Customer_Record(self):
        self.strg='Name                    Price                             Details'
        name=input('Enter username of the customer: ')
        print()
        list_files=os.listdir()
        if (name+'.txt') in list_files:
            
            try:

                f=open(name+'.txt','r')
                self.record=f.readlines()
                for i in self.record:
                    i=i.strip()
                    print('User\'s Email:',self.record[0])
                    print('User\'s Password:',self.record[1])
                    print('User\'s Name:',self.record[2])
                    self.record=i.split(',')
                    self.strg+=f'\n{self.record[0]:30}{self.record[1]:30}{self.record[2]:30}'
                print(self.strg)
            except:
                f=open(name+'.txt','r')
                self.record=f.readlines()
                self.record=self.record[3:]
                for i in self.record:
                    i=i.strip()
                    self.record=i.split(',')
                    self.strg+=f'\n{self.record[0]:30}{self.record[1]:30}{self.record[2]:30}'
                print(self.strg)  

        
l=Login()
