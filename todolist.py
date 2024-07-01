import string
import json

todo_file = open ("todolist.json")
todolist = json.load(todo_file)

def print_to_do_list(message):
    print(message)
    for todo in range(0,len(todolist)):
        todo_done = ""
        if todolist[todo][1] == True:
            todo_done = "■"
        else:
            todo_done = "□"
        print(str(todo+1)+"-- "+todolist[todo][0]+" "+todo_done)

def ask_action():
    print("What would you like to do?")
    print("[X] check a to-do as done, [A] add a to-do, [R] remove a to-do, [S] show the list, [C] Clear the to-do list, [Q] Quit the program, saving the list")

    action_input = input("---> ")

    match action_input.lower():
        case "x":
            print("Which to-do do you want to check?")
            todo_to_check = int(input("Index of To-do ---> "))
            todolist[todo_to_check-1][1] = True
            print_to_do_list("This is the new to-do list")
            ask_action()

        case "a":
            print("Nice!, now please write the to-do")
            new_todo = input("---> ")
            print(new_todo)
            todolist.append([new_todo, False])
            print_to_do_list("This is your new to-do list")
            ask_action()

        case "r":
            print("Nice, which to-do would you like to remove?")
            todo_to_remove = int(input("Index of To-do ---> "))
            todolist.pop(todo_to_remove-1)
            print_to_do_list("This is the new to-do list")
            ask_action()
        
        case "c":
            print("Holy hell, you sure to clear the entire list?")
            response = input("ya sure? [Y]/[N] ---> ")
            match response.lower():
                case "y":
                    print("Alright")
                    todolist.clear()
                    print_to_do_list("Ya happy?")
                    ask_action()
                case "n":
                    print("Alright thank god")
                    ask_action()

        case "s":
            print_to_do_list("Here it is")
            ask_action()
        
        case "q":
            with open("todolist.json", "w") as file:
                json.dump(todolist, file)


        case _:
            print("This action is not valid")
            ask_action()

print_to_do_list("Hi, this is your current To-Do list:")
ask_action()

