
# import pickle

# with open('data.pickle', 'rb') as fh:
#     todos = pickle.load(fh)

# def change(priority, index,newValue):
#     todos[priority][index] = newValue

# def add_task():
#     task = input("Enter an item to add to the to-do list. \n")
#     return task
    
# def priority_request():
#     while True:
#         priority = input("Enter priority for this task (High, Medium or Low) : \n")
#         return priority
# def see_list(list):
#     count = 1
#     for key, value in todos.items():
#         index = 0
#         for index in range(len(value)):
#             item = list[key][index]
#             print(f"{count}: {item}-{key}")
#             count += 1
#             index += 1

# def del_list2():
#     see_list(todos)
#     priority = input('What is the priority of the task? : \n')
#     count=1
#     for item in todos[priority]:
#         print(f"{count}:{item}")
#         count += 1
#     num = input("What is the item number you want to delete? : \n")
#     index = int(num) -1
#     del todos[priority][index]


# while True:
#     main_menu = input('''****** Main Menu ******

# Input 1 to add a task.

# Input 2 to delete a task.

# Input 3 to view all saved tasks.

# Input q to quit program.
#     ''')

#     if main_menu == '1':
#         priority = priority_request()
#         task = add_task()
#         todos[priority].append(task)
#         print(todos)
        
#     elif main_menu == '2':
#         del_list2()
        
#     elif main_menu == '3':
#         see_list(todos)

#     elif main_menu == 'q':
#         with open('data.pickle', 'wb') as fh:      
#             pickle.dump(todos, fh)
#         break
#     else:
#         print('Invalid Option, please select 1,2,3 or q')




import pickle


# with open('data.pickle', 'wb') as fh:            # wb = write as binary
#     todos = pickle.load(fh)

with open('data.pickle', 'rb') as fh:
    todos = pickle.load(fh)





# def change(priority, index,newValue):
#     todos[priority][index] = newValue

# def update():
#     see_list(todos, prompt = "no"
#     choosing = "yes"
#     while choosing == "yes"


def add_task():
    task = input("Enter an item to add to the to-do list. \n")
    return task
    
def priority_request():
    while True:
        priority = input("Enter priority for this task (High, Medium or Low): \n") 
        if priority == "high" or priority == "medium" or priority == "low":
            return priority
            break
        else:
            print("\nInvalid input. (Input: High, Medium, or Low)\n")
        
        
def see_list(list, prompt):
    count = 1
    for key, value in todos.items():
        index = 0
        for index in range(len(value)):
            item = list[key][index]
            
            print(f"{count}: {item}-{key}")
            count += 1
            index += 1
    if prompt == "yes":
        confirm = input("Press any button to continue. \n")
    else:
        pass

def del_list():
    choosing = "yes"
    while choosing == "yes":
        see_list(todos, prompt ="no")
        task_num = int(input("Enter the number you want to delete \n"))-1;
        try:
            calc_high = len(todos["high"]);
            calc_medium1 = len(todos["high"]);
            calc_medium2 = len(todos["medium"])+len(todos["high"]);
            calc_low = len(todos["medium"])+len(todos["high"]);
            if task_num < calc_high:
                task_priority = "high";
                task_num = task_num;
                bad_item = todos[task_priority][task_num]
                print(f"You deleted {bad_item}\n")
                del todos[task_priority][task_num] 
                choosing = "no"
            elif task_num >= calc_medium1 and task_num < calc_medium2:
                task_priority = "medium";
                task_num = len(todos["high"]) - task_num;
                bad_item = todos[task_priority][task_num]
                print(f"You deleted {bad_item}\n")
                del todos[task_priority][task_num] 
                choosing = "no"
            elif task_num >= calc_low:
                task_priority = "low"
                task_num = (len(todos["medium"])+len(todos["high"])) - task_num
                bad_item = todos[task_priority][task_num]
                print(f"You deleted {bad_item}\n")
                del todos[task_priority][task_num] 
                choosing = "no"
        except:
            print("The number you chose is not on the list. Please choose again.")
    confirm = input("Press any button to continue. \n")



while True:
    main_menu = input('''****** Main Menu ******
Input 1 to add a task.
Input 2 to delete a task.
Input 3 to view all saved tasks.
Input q to quit program.
    ''')

    if main_menu == '1':
        priority_level = priority_request()
        added_task = add_task()
        todos[priority_level].append(added_task)
        confirm = input(f"You added {added_task} to {priority_level} priority. \nPress any button to continue. \n")
        
    elif main_menu == '2':
        del_list()
        
    elif main_menu == '3':
        see_list(todos, prompt="yes")
    
    # elif main_menu == '4':
    #     update()

    elif main_menu == 'q':
        with open('data.pickle', 'wb') as fh:            # wb = write as binary
            pickle.dump(todos, fh)
        break
    else:
        print('\nInvalid Option, please select 1,2,3 or q\n')
        input("Press any button to continue to main menu\n")

