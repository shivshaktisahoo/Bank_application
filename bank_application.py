# ************************************* BANK_APPLICATION **********************************
import ast
class Bank:
    def __init__(self):
        pass

    # User login Function/method
    def signin(self):
        account_id = input(" Enter Your ID/Name ")
        account_pwd = str(input(" Enter Your password: "))
        decison = check_id(account_id,account_pwd)
        x=account_id
        if decison == None:
            x,decison = check_name(account_id,account_pwd)                      # here x is the id
        if decison != None:
            print("We have this account ",decison)
            while(True):
              n=str(input('For DEPOSIT :   type 1\nfor WITHDRAW :  type 2\nfor EXIT:\ttype 0\n'))
              if (n=='1'):
                self.deposit(x)                                                       # here x is the id
              elif (n=='2'):
                self.withdraw(x)
              elif (n=='0'):
                print("**************** Have a Nice Day!!! ********************   ")
                break
              else:
                print('enter correct keyword')
        else:
            print("No such Account")

    # New User Signup Function/method
    def signup(self):
        global d1
        sub_d1 = dict()
        id = max(d1['detail'].keys()) + 1
        sub_d1["Name"] = input('Enter ur name : ')
        sub_d1['Balance'] = 0
        d1['detail'][id] = sub_d1
        d1['auth'][id] =  input('Enter new PIN : ')   
        with open('demo.txt','w') as file1:
             file1.write(str(d1))
        print(f"New Account Created\nId : {id}\nName : {d1['detail'][id]['Name']}\nBalance : {d1['detail'][id]['Balance']}\nPIN : {d1['auth'][id]}\n")
        return d1
    
    def deposit(self,id):                                       # for deposit and updating Balance
        global d1
        id= int(id)
        amount = int(input('Enter deposit amount : '))
        d1['detail'][id]['Balance'] +=amount
        print(d1['detail'][id])
        with open('demo.txt','w') as file1:
            file1.write(str(d1))

    def withdraw(self,id):                                  # for withdrawing and updating Balance
        global d1
        id= int(id)
        amount = int(input('Enter withdraw amount   : '))
        if(d1['detail'][id]['Balance']>=amount):
            d1['detail'][id]['Balance'] -=amount
            print(d1['detail'][id])
        else:
            print('You Have Insufficiant Balance!!!! ')
        with open('demo.txt','w') as file1:
           file1.write(str(d1))



# Checking Name and pasword entered by user is correct or not
def check_name(name,pwd):
    for id, details in d1['detail'].items():
        try:
            if (d1['detail'][id]['Name']).lower() == name.lower():
                if (pwd==d1['auth'][id]):
                    return id,details
                else:
                    print('Wrong Password')     
        except:
            pass
    else:
        return id,None

# Checking ID and pasword entered by user is correct or not
def check_id(id,pwd):
    try:
        id = int(id)
        if(pwd==d1['auth'][id]):
            acc_detail = d1['detail'][id]
            return acc_detail
        else:
            print('Wrong Password')    
    except:
        return None


with open('demo.txt','r') as file1:
    i = file1.read()
    i = ast.literal_eval(i)                                           #converted string to dictinory
d1 = dict(i)
while(True):
    print('\n******************** Welcome To ABC Bank **************************' )
    log = input('For SIGNIN :   type 1\nfor SIGNUP :   type 2\n')
    x = Bank()
    if log == '1':
        x.signin()
        break
    elif log == '2':
        x.signup()
        continue
    else:
        print('press correct keyword')

