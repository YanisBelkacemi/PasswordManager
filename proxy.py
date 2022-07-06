import json

#where our log-in info are stored
accounts_data = dict()
accounts_data["yanis"] = "Yanis12345678yanis"
accounts_data["rayan"] = "Rayan12345678rayan"



#check if you have an account

doYou = input("do you have an account (Y/N) : ")




#DataBase That the user wants to access as json

with open("data.json","r") as f:
    data = json.load(f)

#check if you have an account or this is your first time
def check_for_account():
    if doYou == 'y':
        login()
    if doYou == 'n':
        sign_in()
    else:
        print("I cant reconize your command ")





#sign-in
def sign_in():
    sign_name = input('please Enter the name that you want to assign for your account : ')
    sign_password = input('please enter the password that you want to assign to your account : ')
    if sign_name not in accounts_data:
        accounts_data[sign_name] = sign_password
        print("your account has been created!")
        login()
    else:
        print("choose another name ")
        sign_in()







#function that will check the infos
def login():
    # to input our logni infos
    _accname = input("enter your name : ")
    _accpassword = input("enter your password : ")

#check if the entered login info are the same with those in the login database
    if _accname in accounts_data.keys() and _accpassword in accounts_data.values():
        if _accname in data:
            print(data[_accname])
        else:
            print("we cant find data with name:" , _accname)

#if the name is incorrect but the password is correct
    elif _accname not in accounts_data.keys():

        print('your name is incorrect please Retry !')

#if the password is incorrect but the name is correct
    elif _accpassword not in accounts_data.keys():

        print('your name is incorrect please Retry !')






check_for_account()
