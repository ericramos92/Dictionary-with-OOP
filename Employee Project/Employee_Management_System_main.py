import Employee_Management_System
import pickle


def main():
    file_employ_dic = load_employee_id()
    choice = 0

    while(choice != 5):
        choice = menuitems()
        if choice == 1:
            lookup(file_employ_dic)
        elif choice == 2:
            addEmployee(file_employ_dic)
        elif choice == 3:
            changeemployee(file_employ_dic)
        elif choice == 4:
            deleteemployee(file_employ_dic)
        elif choice == 5:
            quitemployee(file_employ_dic)


#functions
def load_employee_id():
    try:
        input_field = open('employee.dat','rb')
        id_dic = pickle.load(input_field)
        input_field.close()
    except IOError:
        id_dic = {}
    return id_dic

def menuitems():
    print("Please Pick one....")
    print("Look uo Employee--Type 1")
    print("Add employee--Type 2")
    print("Change an existing Employee--Type 3")
    print("Delete an employee--Type 4")
    print("Quit--Type 5")
    choice = int(input("Enter choince:"))
    if choice < 0 or choice > 5:
        choice = int(input("Please enter valid number from 1-5:"))
    return choice

def lookup(employee_dic):
    #ask for # ID
    print("This is look up")
    id = int(input("Please enter ID:"))
    if id in employee_dic:
        print("I HAve found the info for the employee with the ID: " + str(id))
        print("--------------------------------------------")
        print(employee_dic.get(id))
    else:
        print("Sorry there is not employee with that ID")

def addEmployee(employee_dic):
    id = int(input("Please enter ID:"))
    name = input("Please enter Name:")
    department = input("Please enter Department:")
    job = input("Please enter Job:")
    obj = Employee_Management_System.employee(name,id,department,job)
    if id not in employee_dic:
        employee_dic[id] = obj
        print("Employee has been added!!!")
        print(employee_dic[id])
    else:
        print("This Emplyee already exits")
def changeemployee(employee_dic):
    print("Please enter ID of the employee that you want to change the info.")
    id = int(input("ID:"))
    if id in employee_dic:
        print("New information for employee")
        name = input("Please enter Name:")
        department = input("Please enter Department:")
        job = input("Please enter Job:")
        obj = Employee_Management_System.employee(name,id,department,job)
        employee_dic[id] = obj
        print("The information has been updated!")
    else:
        print("The Id was not found")

def deleteemployee(employee_dic):
    print("PLease enter the Id you would like to delete")
    delete_item = int(input("Enter ID:"))
    if delete_item not in employee_dic:
        print("The ID was not found")
    else:
        del employee_dic[delete_item]
        print("The ID has been deletd")

def quitemployee(employee_dic):
    print("You have quited the program")
    file = open('employee.dat', 'wb')
    pickle.dump(employee_dic,file)
    file.close()
main()
