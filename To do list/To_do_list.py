import json

try:
    with open("tasks.txt" , "r") as file:
        tasks = file.read().splitlines()
except FileNotFoundError:    
    tasks = []
    
    def write_task():
         with open("tasks.json" , "w") as file:
            json.dump(tasks ,file ,indent = 4)
        
while True:
    print("\n====== TO DO LIST ======")
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Exit")
    
    
    choice = input("Enter your choice: ")
    
    if(choice == "4"):
        print("Goodbye!!")
        break
    
    if(choice == "1"):
        task = input("Enter your task: ")
        tasks.append(task)
        write_task()   
        print("Task added succesfully!!!")  
        input("\nPress Enter to return to the menu...")
        
    if choice == "2":
        if len(tasks) == 0:
            print("No tasks available!")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}") 
                
        input("\nPress Enter to return to the menu...")    
        
    if choice == "3":
        if len(tasks) == 0:
            print("No tasks available!")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

            delete = int(input("Enter the task number you want to delete: "))

            if 1 <= delete <= len(tasks):
                tasks.pop(delete - 1)
                write_task()
                print("Task deleted successfully!")
            else:
                print("Invalid task number!")
        input("\nPress Enter to return to the menu...")
                
    if choice not in ["1","2","3","4"]:
        print("Invalid Choice!!!")
        input("\nPress Enter to return to the menu...")                
