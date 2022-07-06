import json

accounts_data = dict()

#add new users
def dumper():
    with open("user_info.json", "w") as user:
        json.dump(accounts_data, user, indent=2)
with open("user_info.json", "r") as password:
    user_info = json.load(password)



#check if you have an account

doYou = input("do you have an account (Y/N) : ")




#DataBase That the user wants to access as json

with open("data.json", "r") as f:
        data = json.load(f)




#check if you have an account or this is your first time
def check_for_account():
    if doYou == 'y':
        login()
    if doYou == 'n':
        sign_in()







#sign-in
def sign_in():


    sign_name = input('please Enter the name that you want to assign for your account : ')
    sign_password = input('please enter the password that you want to assign to your account : ')



    if sign_name not in user_info:
        accounts_data[sign_name] = sign_password
        dumper()
        print("your account has been created!")



    else:
        print("choose another name ")
        sign_in()







#function that will check the infos
def login():
    # to input our logni infos
    _accname = input("enter your name : ")
    _accpassword = input("enter your password : ")


#check if the entered login info are the same with those in the login database
    if _accname in user_info:
        intent_data= json.dumps(data , indent=2)
        print(intent_data)


#if the name is incorrect but the password is correct
    elif _accname not in user_info.keys():

        print('your name is incorrect please Retry !')


#if the password is incorrect but the name is correct
    elif _accpassword not in user_info.keys():

        print('your name is incorrect please Retry !')


check_for_account()
dumper()