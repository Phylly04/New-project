from datetime import datetime

#defining functions at the top for my code 
#and calling them at the bottom when i need to work with them

def reg_user():
    while True:
        new_username = input("Enter your username: ")
        new_password = input("Enter your password: ")
        password_confirm = input("confirm password: ")
#if the user who logged in is admin then it continues to run and register other users
# ask user for username and password
# checking if password matches confirmation

        while new_password != password_confirm:
            print("Passwords does not match, please try again.")
            
            
            password_confirm = input("Confirm your password: ")
        
# Checking if username and password already exist
        if new_username in usernames:
            print("Username already exists. Please try another username.")
        else:
            # Writing username and password to text file
            with open('user.txt', 'a') as file:
                file.write('\n' +new_username +', '+new_password)
                print("\nUser registered successfully.\n")
                break

#This function will be called when a user adds a task
def add_task():
        persons_username = input("Enter persons username: ")
        task_title = input("Enter title of task:" )
        task_description = input("Enter task_discription: ")
        
        # Get the current date in "%d %b %Y" format
        current_date = datetime.today().strftime('%d %b %Y')
        date_format = '%d %b %Y'
        # Get the due date from user input in "%d %b %Y" format
        due_date_str = input("Enter due date in 'DD MMM YYYY' format: ")

        # Converting the user input to a datetime object using strptime
        due_date = datetime.strptime(due_date_str, date_format).strftime('%d %b %Y')
        task_completed_or_not = "No"
        

        file = open("tasks.txt", "a")
        file.write("\n"+ persons_username + ", "+ task_title +", "+task_description + ", "+current_date  + ", "+ due_date +", "+task_completed_or_not)
        file.close()
        print("\ntask successfully added!!! \n")

  
#This function is called when viewing all added taskst
def view_all():
       with open("tasks.txt","r") as read_file:
            file_read = read_file.readlines()
            
       
            for index, line in enumerate(file_read):
                 va_line =line.strip().split(", ")
                 print(f"""
Task:           {index + 1}
Assign To:      {va_line[0]}
Task Name:      {va_line[1]}
Task Description: {va_line[2]}
Date Assign:    {va_line[3]}
Due Date:       {va_line[-2]}
Task Complete:   {va_line[-1]}


""" )


 #a user will call this function when viewing their tasks     
def view_mine(user_name):
        
        # Open the task.txt file and read the contents
        with open("tasks.txt", "r") as read_file:
            tasks = read_file.readlines()

        # Iterate through the tasks and find those assigned to the user
        user_tasks = []

        for index, task in enumerate(tasks):

            task_details = task.strip().split(", ")
            assigned_to = task_details[0].strip()
            task_name = task_details[1].strip()
            task_description = task_details[2].strip()
            Date_assigned = task_details[3].strip()
            Due_date = task_details[-2].strip()
            task_completed_or_not = task_details [-1].strip()
            task_num = index +1

        
            if assigned_to == user_name:
                user_tasks.append((task_num, task_name, task_description, Date_assigned, Due_date, task_completed_or_not))

                

        # Displaying the tasks assigned to the user
        if user_tasks:
            print(f"Tasks assigned to {user_name}:")
            for task in user_tasks:
                print(task)
        else:
            print(f"No tasks assigned to {user_name}.")  


          

        # Ask the user to select a task number or -1 to return to the main menu
        while True:
            
            task_num = input("\nEnter a task number or -1 to return to the main menu: ")
        
            if task_num == "-1":
                break
            # Check if the task number entered by the user is valid
            elif not task_num.isdigit() or int(task_num) < 1 or int(task_num) > len(tasks):
                print("Invalid task number. Please try again.")

            else:
                task_index = int(task_num) - 1
                task = tasks[task_index].split(", ")

                if not task[0] == user_name:
                    print("You have entered an incorrect task number, please try again")
                    continue
                print(f"Selected task: {task}")
            
                task_name = task[1]
                task_description = task[2]
                date_assigned = task[3]
                due_date = task[4]
                task_completed_or_not = task[5]

                # Ask the user if they want to mark the task as complete, change the assigned user, or change the due date
                action = input(" \nEnter 'complete' to mark the task as complete, 'change user' to change the assigned user, or 'change date' to change the due date: \n")
                
                if action == "complete":
                    if task_completed_or_not == "Yes":
                        print("Task is already completed.")
                    else:
                        tasks[task_index] = f"{user_name}, {task_name}, {task_description}, {date_assigned}, {due_date}, Yes\n"
                        with open("tasks.txt", "w") as file:
                            file.writelines(tasks)
                        print("Task marked as complete.")

                elif action == "change user":
                    new_user_name = input("Enter the new user name: ")
                    tasks[task_index] = f"{new_user_name}, {task_name}, {task_description}, {date_assigned}, {due_date}, {task_completed_or_not}\n"
                    with open("tasks.txt", "w") as file:
                        file.writelines(tasks)
                    print("Assigned user changed.")

                elif action == "change date":
                    new_due_date = input("Enter the new due date ( DD MM YYYY): ")
                    tasks[task_index] = f"{user_name}, {task_name}, {task_description}, {date_assigned}, {new_due_date}, {task_completed_or_not}\n"
                    with open("task.txt", "w") as file:
                        file.writelines(tasks)
                    print("Due date changed.")
                
                else: 
                    print("Invalid action. Please try again.")

        print() # Printing an empty line for formatting purposes.

  
# This function will be called when user wants to see the stats 
# about the number of users logged in and number of tasks

def display_stats():

         # Opening the tasks file and read the lines
        with open('tasks.txt', 'r') as tasks_file:
            tasks_lines = tasks_file.readlines()

        # Counting the number of lines in the tasks file
        num_tasks = len(tasks_lines)

        # Open the users file and read the lines
        with open('user.txt', 'r') as users_file:
            users_lines = users_file.readlines()

        # Counting the number of lines in the users file
        num_users = len(users_lines)

        # Printing the results
        print("Number of tasks: ", num_tasks)
        print("Number of users: ", num_users)
        #i opened the text files, read from them then counted the number of tasks as well as
        # number of users registered bu using the len built in funtion


#====Login Section====
# in this section the admin will be able to login 
# i made use of while loop to validate your user name and password.

usernames = []
passwords = []

with open ("user.txt", "r") as user_file:
    for line in user_file:
        
        user, pas =line.strip("\n").split(", ")
        #in this section i opened the file, stripped and split
        #the line in the file with username and password
        
        usernames.append(user) #i then appended the username as well as the password
        passwords.append(pas)

user_name = input("enter username: ") 

#i made use of while loop to loop through invalid password and user
 #until correct credentials are entered

while not user_name in usernames:
    print("invalid username")
    user_name = input("enter username: ")   

password_index = usernames.index(user_name)
pass_word = input("enter password: ")  

while pass_word != passwords[password_index]:
    print("invalid password")
    pass_word = input("enter password: ")  

#after the user has been logged in they will choose any of the options below to proceed
#if they chose an option that is not listed below it will ask them to enter correct option

while True:

    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - generate reports
ds - display statistics
dr - display report statistics
e - Exit
: ''').lower()
    
    if menu == 'r':#registering a user using the nested loops
        if user_name == "admin": #only user with usernmae admin can register users!!
            reg_user()
        else:
            print("\nOnly admin can register a user!!")
            
    elif menu == 'a':#adding a task to the task txt file using "a" to add collected tasks information to task file
        add_task()

    elif menu == 'va': #displaying task information on screen
      view_all()

    elif menu == "vm":#displaying tasks that are assigned to the user that is loggen in
       view_mine(user_name) 
                   
    elif menu == "gr":
        #this section will generate reports and save them to task_overview.txt 
        # as well as user_overview.txt

        with open('tasks.txt', 'r') as tasks_file:
            tasks_lines = tasks_file.readlines()
            # i firstly opened the file and read from it

        # Counting the number of lines in the tasks file
        num_tasks = len(tasks_lines)
   
         #calculating the number of completed taskts
        with open("tasks.txt", "r") as read_file:  
            line_read = read_file.readlines()
            count = 0 
            # initialize a counter variable to keep track of the number
            # of "yes" occurrences

            for lines in line_read:
                line = lines.strip("\n").split(", ")
                last_element = line[-1]
                if "yes" in last_element:
                    count += 1 
            # incremented the counter variable by 1 if "yes" is found in the last
            #  element

      #finding and calculating the number of uncompleted tasks
                
        with open("tasks.txt", "r") as read_file:
            line_read = read_file.readlines()
            count_no = 0
            for lines in line_read:
                line = lines.strip("\n").split(", ")
                last_element = line[-1]
                if "no" in last_element.lower():
                    count_no += 1

#calculating the number of uncompleted tasks that are overdue
# as well as calculating the percentage of uncompleted tasks 

        with open("tasks.txt", "r") as read_file:
            line_read = read_file.readlines()
            count_overdue = 0
            count_uncompleted = 0

            # Defining today's date 
            
            today  = datetime.today().strftime('%d %b %Y')

            for lines in line_read:
                line = lines.strip("\n").split(", ")
                last_element = line[-1]
                due_date = line[-2]
                if "no" in last_element.lower() and due_date < str(today):
                    count_overdue += 1
                if "no" in last_element.lower():
                    count_uncompleted += 1

# the last element contains completetion status and if theres no it means
# the task is incomplete, i also checked if the date is due by using arithmetic operation
#< to check if it is less than todays date

            total_tasks = len(line_read)
            percent_overdue = round((count_overdue / total_tasks) * 100,2)
            percent_uncompleted = round((count_uncompleted / total_tasks) * 100,2)

# finally writing all the collected and generated reports to task.overview file

        with open("task_overview.txt","a") as file:
            file.write("\n"+ "Number of tasks: "+ str(num_tasks) + "\n" + "Number of completed taskst: "+  str(count) + "\n"+
                       "Number of uncompleted tasks: " + str(count_no) +"\n" + "Number Of Uncompleted and overdue tasks: " +  str(count_overdue) +
                       "\n" + "Percentage of uncompleted tasks: "+ str(percent_uncompleted)+"%" + "\n" + "Percentage of overdue tasks: " + str(percent_overdue)+ "%")
            
            print("\nadded to task_overview.txt file successfully!!!\n")

#Writing to user_overview.txt file
        with open('user.txt', 'r') as users_file:
            users_lines = users_file.readlines()

# Counting the number of lines in the users file
        num_users = len(users_lines)

        with open('tasks.txt', 'r') as tasks_file:
            tasks_lines = tasks_file.readlines()

 # Counting the number of lines in the tasks file
        num_tasks = len(tasks_lines)

# Reading user data from user.txt file
        user_data = {}
        with open('user.txt', 'r') as users_file:
            for line in users_file:
                user_info = line.strip().split(',')
                username = user_info[0]
                user_data[username] = 0

# Counting the number of tasks assigned to each user
        with open('tasks.txt', 'r') as tasks_file:
            for line in tasks_file:
                task_info = line.strip().split(', ')
                username = task_info[0]
                if username in user_data:
                    user_data[username] += 1

# Calculating the percentage of the total number of tasks assigned to each user and 
# writing to file
        with open('user_overview.txt', 'w') as f:
            for username, count in user_data.items():
                task_percentage = round((count/num_tasks)*100)
                f.write( username+ ":"+ str(count)+ " "+"tasks assigned"+ "\n")
                f.write(f"percentage of tasks assigned for user {username}: {task_percentage} %\n")
                
# Calculating the percentage of completed tasks assigned to each user and 
# writing to file
                
                completed_count = 0
                for line in tasks_lines:
                    task_info = line.strip().split(', ')
                    if task_info[0] == username and task_info[-1] == 'yes':
                        completed_count += 1
                if completed_count ==0:
                    completed_percentage = round((completed_count)*100,2)
                    f.write(f"percentage of completed tasks for user {username} is {completed_percentage} %\n")
                else:
                    completed_percentage = round((completed_count/count)*100,2)
                    f.write(f"percentage of completed tasks for user {username} is {completed_percentage} %\n")                      
 # Calculating the percentage of uncompleted tasks assigned to each user and
 #  writing to file
                
                uncompleted_count = count - completed_count
                if uncompleted_count == 0:
                    uncompleted_percentage = round((uncompleted_count)*100,2)
                    f.write(f"percentage of uncompleted tasks for user {username} is {uncompleted_percentage} %\n")
                else:
                    uncompleted_percentage = round((uncompleted_count/count)*100,2)
                    f.write(f"percentage of uncompleted tasks for user {username} is {uncompleted_percentage} %\n")

# Calculating the percentage of overdue and uncompleted tasks assigned to each
#  user and writing to file
                
                overdue_count = 0
                for line in tasks_lines:
                    task_info = line.strip().split(', ')
                    today_date = datetime.today().strftime('%d %b %Y')
                    
                    if task_info[0] == username and task_info[-2] < str(today_date) and task_info[-1] == 'no':
                        overdue_count += 1
                if overdue_count ==0:
                    overdue_uncompleted_percentage = round((overdue_count)*100,2)
                    f.write(f"percentage of overdue and uncompleted tasks for user {username} is {overdue_uncompleted_percentage} %\n")
                else:
                    overdue_uncompleted_percentage = round((overdue_count/count)*100,2)
                    f.write(f"percentage of overdue and uncompleted tasks for user {username} is {overdue_uncompleted_percentage} %\n")

            print("\n Sucessfully added to user_overview.txt file !!!\n")

    elif menu == "dr":
        #This section will display the generated reports from the two files
        # task_overview.txt as well as user_overview.txt fileS


        with open("task_overview.txt","r") as read_file:
            lines = read_file.readlines()
            
            for lines in lines:
                lines_info = lines.split("\n"", ")
                
                print(lines_info,"\n")
            print("Reports successfully displayed for task_overview.txt !!!")
        
        with open("user_overview.txt","r") as read_file:
            lines = read_file.readlines()
            for lines in lines:
                lines_data = lines.split("\n"", ")
            
                print(lines_data,"\n")
            print("Reports successfully displayed for user_overview.txt file: ")
        print("generage reports first if not generated on gr:")
       
    elif menu == "ds":
#This section displays the statistics 
# formatting and calculating each time a new user is registered or logs in
#this section will count the number of times a user is registered
                
        display_stats()

                    
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")