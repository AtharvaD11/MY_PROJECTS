
#Please run this program in terminal
#Before running please type 'pip install stdiomask' and install stdiomask module in your system

import pickle
import stdiomask
import os
def display_welcome():
    os.system('cls')
    print("\n\n\t\t\t\t@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("\t\t\t\t|                                                          |")
    print("\t\t\t\t|                                                          |")
    print("\t\t\t\t|                        WELCOME  TO                       |")
    print("\t\t\t\t|                  HOSPITAL MANAGEMENT SYSTEM              |")
    print("\t\t\t\t|                                                          |")
    print("\t\t\t\t|                                                          |")
    print("\t\t\t\t@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n")
    os.system("pause")



def login_page():
    print("\n\n                       HOSPITAL MANAGEMENT SYSTEM            ")
    print("                         -----------------------------          ")
    print("                                     LOGIN                      ")
    print("                         -----------------------------          ")

def menu():
    print("                            HOSPITAL MANAGEMENT SYSTEM\n\n")
    print("                Please, choose from the following options.\n")
    print("\t--------------------------------------------------------------------")
    print("\t|                                                                  |")
    print("\t|               1 >> Add new patient record.                       |")
    print("\t|               2 >> Display information of patient.               |")
    print("\t|               3 >> Update patient's information.                 |")
    print("\t|               4 >> Exit the program.                             |")
    print("\t|                                                                  |")
    print("\t--------------------------------------------------------------------")

def Insert(F):
    try:
        file = open(F,'ab+')
        if file.tell()>0:
            file.seek(0)
            Record1 = pickle.load(file)
        else:
            Record1 = []
        #print(Record1)
        while True:
            print("\n***********************************************\n")
            Name = input("Name:  ").upper()
            Age = int(input("Age:  "))
            Gender = input("Gender:  ")
            Blood_Group = input("Blood Group:  ")
            Address = input("Address:  ")
            Contact = input("Contact Number:  ")
            Earlier = input("Any major disease suffered earlier?(If yes please specify):  ")
            Pat_ID = input("Patient ID:  ")
            print("\n*******************************************")
            Rec = [Name,Age, Gender,Blood_Group,Address,Contact,Earlier,Pat_ID]
            Record1.append(Rec)
            ch = input("Do you want to enter new record?")
            if ch == "n" or ch =='N':
                print("Information saved successfully.\n")
                break
        os.system('pause')
        os.system('cls')
        file.close()
        with open(F,'wb') as file:
            pickle.dump(Record1,file)
    except ValueError:
        print("Invalid values entered.")

def ThankYou():
    os.system('cls')
    print("\n\n\t\t\t\t@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("\t\t\t\t|                                                          |")
    print("\t\t\t\t|                                                          |")
    print("\t\t\t\t|                    THANK YOU FOR USING                   |")
    print("\t\t\t\t|                 HOSPITAL MANAGEMENT SYSTEM               |")
    print("\t\t\t\t|                                                          |")
    print("\t\t\t\t|                                                          |")
    print("\t\t\t\t@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n")


def Display(F): #Function to Display the records in the Binary File
    try:
        with open(F,'rb') as fil:
            Rec=pickle.load(fil)
            c=len(Rec)
            #print(Rec)
            lst = ['Name', 'Age','Gender','Blood Group','Address','Contact Number','Any Major Disease Suffered Earlier(If yes please specify)',"Patient ID"]
            inp = input("Enter the name of patient to be displayed:  ")
            print("*****************************************")

            for i in range(c):
                if Rec[i][0] == inp.upper():
                    for j, k in zip(lst,Rec[i]):
                        print(j, " :  ",k)
                    break
            else:
                print("Record not found!")
            print("****************************************")
    except FileNotFoundError:
        print(F, "File Doesn't exist")
    os.system('pause')
    os.system('cls')

def Update(F):
    try:
        with open(F,'rb+') as file:
            Rec = pickle.load(file)
            found = -1
            A = input("Enter the name of the patient whose record is to be updated:  ")
            for i in Rec:
                if i[0] == A.upper():
                    found = 0
                    ch = input("Update Name(Y/N)?  ")
                    if ch =='y' or ch == 'Y':
                        i[0] = input("Enter Name: ").upper()

                    ch = input("Update Age(Y/N)?  ")
                    if ch == 'y' or ch == 'Y':
                        i[1] = int(input("Enter Age: "))

                    ch = input("Update Gender(Y/N)?  ")
                    if ch == 'Y' or ch =='y':
                        i[2] = input("Enter Gender: ")

                    ch = input("Update Blood Group(Y/N)?  ")
                    if ch == 'Y' or ch =='y':
                        i[3] = input("Enter Blood Group: ")

                    ch = input("Update Address(Y/N)?  ")
                    if ch == 'Y' or ch =='y':
                        i[4] = input("Enter Address: ")

                    ch = input("Update Contact Number(Y/N)?  ")
                    if ch == 'Y' or ch =='y':
                        i[5] = int(input("Enter Contact Number: "))

                    ch = input("Update 'Major diseases suffered earlier'(Y/N)?  ")
                    if ch == 'Y' or ch =='y':
                        i[6] = input("Enter Any Major Disease Suffered Earlier(If yes please specify): ")

                    ch = input("Update Patient's ID(Y/N)?  ")
                    if ch == 'Y' or ch =='y':
                        i[7] = input("Enter Contact Number: ")
            print("\nPatient's details have been updated successfully...\n")
            if found == -1:
                print("Patient details not found\n")
            else:
                file.seek(0)
                pickle.dump(Rec,file)

    except EOFError:
        pass
    except FileNotFoundError:
        print(F, "File does not exist.")
    os.system('pause')
    os.system('cls')


Fi = "Hospital"
display_welcome()
os.system('cls')
login_page()
inp = stdiomask.getpass("           Enter password: ")
while True:
    if inp == 'pass':
        print("           Access Granted!!!")
        os.system("pause")
        os.system('cls')
        while True:
            try:
                menu()
                ch = int(input("             Enter your choice:  "))
                if ch == 1:
                    Insert(Fi)
                elif ch == 2:
                    Display(Fi)
                elif ch == 3:
                    Update(Fi)
                elif ch == 4:
                    ThankYou()
                    os.system('pause')
                    os.system('cls')
                    break
                else:
                    print("Invalid Choice Entered.")
                    os.system('pause')
                    os.system('cls')
            except ValueError:
                print("Invalid choice")
                os.system('pause')
                os.system('cls')

        break
    else:
        print("            Access aborted.")
        print("            Please try again......\n\n")
        os.system('pause')
        os.system('cls')
        login_page()
        inp = stdiomask.getpass("           Enter password: ")


