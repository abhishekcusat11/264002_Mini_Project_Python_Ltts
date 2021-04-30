from FUNCTION import *
print("\n\t|**********************************************|")
print("\n\t|++++++++++++++++++++++++++++++++++++++++++++++|")
print("\n\t| Welcome to StepIn Record Management System   |")
print("\n\t|++++++++++++++++++++++++++++++++++++++++++++++|")
print("\n\t|**********************************************|")
print("\nEnter\n1 To Add new Candidate, \n2 To Display All Candidate, \n3 To Delete existing Candidate, \n4 To Edit a Candidate information, "
      "\n5 To Search for existing Candidate and \n6 To Exit\n")
print("|************************************************************************************************|")
while True:
    
    ch = input("Enter your Option to proceed\n")
    if ch == '1':
        add_new_Data()
    elif ch == '2':
        show_Data()
    elif ch == '3':
        delete_Data()
    elif ch == '4':
        edit_Data()
    elif ch == '5':
        find_Data()
    elif ch == '6':
        print("Thank You For Being The Part Of StepIn")
        exit()
    else:
        print("\nIncorrect Option is chosen. Please enter the correct option again \n")
