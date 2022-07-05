#where our log-in info are stored
accounts_data = dict()
accounts_data["yanis"] = "Yanis12345678yanis"
accounts_data["rayan"] = "Rayan12345678rayan"
#to inputour logni infos
name = input("enter your name : ")
password = input("enter your password : ")

#DataBase That the user wants to access
Data_base = {
        "yanis":{
            "name":name,
            "age" : 17,
            "membership": True

        },


        "rayan":{
            "name":name,
            "age" : 14,
            "membership" : True,
        }
}

def check_for_accounts(_accname,_accpassword):
    _accname = name
    _accpassword = password


    
#check if the entered login info are the same with those in the login database
    if _accname in accounts_data.keys() and _accpassword in accounts_data.values():
        print(Data_base[name])

#if the name is incorrect but the password is correct
    elif _accname not in accounts_data.keys():

        print('your name is incorrect please Retry !')

#if the password is incorrect but the name is correct
    elif _accpassword not in accounts_data.keys():

        print('your name is incorrect please Retry !')


#calls the function
check_for_accounts(name,password)




