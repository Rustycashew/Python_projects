import string
import secrets
import json



try:
    with open("passwords.json" , "r") as file:
        passwords = json.load(file)
        
except (FileNotFoundError, json.JSONDecodeError):
    passwords = {}        


def save_passwords():
     with open("passwords.json", "w") as file:
        json.dump(passwords, file , indent=4)
    

while True:
    print("======== PASSWORD MANAGER ========")
    print("1. Add Password")
    print("2. View Password")
    print("3. Search Password")
    print("4. Update Password")
    print("5. Delete Password")
    print("6. Generate Password")
    print("7. Exit")



    ch = input("Enter your choice: ")
    
    
    if (ch=="1"):
        account = input("Enter Account name: ")
        if (account == ""):
            print("Account name cannot be empty.")
        elif (account in passwords):
            print("Account already exists!")
        else:
                                
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            
            passwords[account]= {
                "username" : username,
                "password" : password   
            }
            print("Password added succesfully!!")
            
            save_passwords()
            
        
        
        input("\nPress Enter to return to the menu")
        
        
    elif (ch=="2"):
       if len(passwords)==0:
           print("No Password saved at the moment!")
       else:
           for account,details in passwords.items():
               print("\nAccount: ", account)
               print("Username: ", details["username"])
               print("Password: ", details["password"])
               
                      
       input("\nPlease Enter to return to the menu")
                  
    elif(ch=="3"):
        account = input("Enter the account you want to search: ")
        if account in passwords:
            print("Account: ", account)
            print("Username: ", passwords[account]["username"])
            print("Password: ", passwords[account]["password"])
        else:
            print("Account not found!.")    
            
        input("\nPress Enter to return to the menu")
                
                
    elif(ch=="4"):
        account = input("Enter the account you want to update: ")
        if account in passwords:
            new_password = input("Enter the new password: ")
            passwords[account]["password"] = new_password
            save_passwords()        
            print("Password updated succesfully!!!")
        else:
            print("Not found!.")
            
            
        input("\nPress Enter to return to the menu")    
                       
    elif(ch=="5"):
        delete = input("Enter the account which you want to delete: ")
        
        if delete in passwords:
            print("1.Yes")
            print("2.No")
            confirm = input(f"Are you sure you want to delete {delete}?: ")
            if (confirm == "1"):
                del passwords[delete]
                print("Account deleted succeslfully!!")
                save_passwords()
            elif(confirm == "2"):
                print("Deletion Cancelled!!")
            else:
                print("Invalid Choice detected!!!")       
        else:
            print("Account not found!.")
            
        input("\nPress Enter to return to the menu")        
        
        
    elif(ch=="6"):
        
        characters = string.ascii_letters + string.digits + string.punctuation
        try:
            length = int(input("Enter the length of the password you require: "))
            key = []
            if (length > 0 and length <12):
                for i in range(length):
                    key.append(secrets.choice(characters))
                    
                final_password = "".join(key)
                print("Generated Password: ", final_password)
            else:
                print("Please enter a valid length for the password.")    
        except ValueError:
            print("Invalid input please enter a number!")
            
            
        input("\nPress Enter to return to the menu")    
        
        
    elif(ch=="7"):
        print("Goodbye!.")
        break
        
                      
    else:
        print("Invalid Option Chosen!")     
        
        