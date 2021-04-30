import os
import pickle

class StepInRecord:
    def __init__(self, name, email_id, phone_no, address):
        self.name = name
        self.email_id = email_id
        self.phone_no = phone_no
        self.address = address

    def __str__(self):
        return "Candidate_ID.:{0}\nEmail_Id.:    {1}\nMobile_No.:   {2}\nTrack.:       {3}\n".format(self.name,self.email_id,self.phone_no,self.address)

    def change_email_id(self, email_id):
        self.email_id = email_id

    def change_name(self, name):
        self.name = name

    def change_phone_no(self, phone_no):
        self.phone_no = phone_no

    def change_address(self, address):
        self.address = address


def add_new_Data():
    RECORD = open("RECORD", "rb")
    is_file_empty = os.path.getsize("RECORD") == 0
    if not is_file_empty:
        Data_list = pickle.load(RECORD)
    else:
        Data_list = []
    try:
        Data = get_Data_data()
        RECORD = open("RECORD", "rb+")
        Data_list.append(Data)
        pickle.dump(Data_list, RECORD)
        print("|************************************************************************************************|")
        print("\n\t\t\t\tNew Record is added successfully\n")
        print("|************************************************************************************************|")
    except KeyboardInterrupt:
        print("Data could not be added")
        return 1
    except EOFError:
        print("Data could not be added")
        return 1
    finally:
        RECORD.close()
        return "new_Data_added"


def get_Data_data():
    try:
        Data_name = input("\nEnter the Candidate ID\n")
        Data_email_id = input("Enter the Email ID \n")
        Data_phone = input("Enter the Mobile number\n")
        Data_address = input("Enter the Track of Candidate (Mechanical/Software/Embedded)\n")
        Data = StepInRecord(Data_name, Data_email_id, Data_phone, Data_address)
        return Data

    except KeyboardInterrupt as e:
        raise e

    except EOFError as e:
        raise e


def show_Data():
    RECORD = open("RECORD", "rb")
    try:
        is_file_empty = os.path.getsize("RECORD") == 0
        if not is_file_empty:
            Data_list = pickle.load(RECORD)
            for Data1 in range(len(Data_list)):
                print()
                print(Data_list[Data1])
            return "displayed"
        else:
            print("\Record is empty\n")
            return "empty"
    except IOError:
        print("\nRecord is not accessible")
    finally:
        RECORD.close()


def find_Data():
    RECORD = open("RECORD", "rb")
    is_file_empty = os.path.getsize("RECORD") == 0
    if not is_file_empty:
        find_name = input("\nEnter the Candidate ID to be searched\n")
        is_Data_found = False
        Data_list = pickle.load(RECORD)
        find(Data_list, find_name, is_Data_found)
    else:
        print("\nSorry Record is empty. Cannot search")
        return "empty"
    RECORD.close()
    return "found"


def find(Data_list, find_name, is_Data_found):
    for Data1 in Data_list:
        Data_name = Data1.name
        find_name = find_name.lower()
        Data_name = Data_name.lower()
        if Data_name == find_name:
            print(Data1)
            is_Data_found = True
            break
    if not is_Data_found:
        print("Searched Data not found")
        return "not_found"


def delete_Data():
    RECORD = open("RECORD", "rb+")
    is_file_empty = os.path.getsize("RECORD") == 0
    if not is_file_empty:
        name = input("\nEnter the Candidate ID to delete\n")
        Data_list = pickle.load(RECORD)
        is_Data_deleted = False
        for i in range(0, len(Data_list)):
            Data1 = Data_list[i]
            if Data1.name == name:
                del Data_list[i]
                is_Data_deleted = True
                print("|************************************************************************************************|")
                print("\nRecord is deleted successfully\n")
                print("|************************************************************************************************|")
                RECORD = open("RECORD", "rb+")
                if len(Data_list) == 0:
                    RECORD.write(b'')
                else:
                    pickle.dump(Data_list, RECORD)
                break
        if not is_Data_deleted:
            print("\nData not found with the searched Candidate ID\n")

    else:
        print("\n Record Manager is empty. Cannot delete Data")
    RECORD.close()


def edit_Data():
    RECORD = open("RECORD", "rb")
    is_file_empty = os.path.getsize("RECORD") == 0
    if not is_file_empty:
        name = input("\nPlease Enter Candidate ID of the Data to be edited\n")
        Data_list = pickle.load(RECORD)
        is_Data_edited = False
        for Data1 in Data_list:
            if Data1.name == name:
                do_edits(Data1)
                RECORD = open("RECORD", "rb+")
                pickle.dump(Data_list, RECORD)
                is_Data_edited = True
                print("\nRecord is edited successfully\n")
                break
        if not is_Data_edited:
            print("Record not found")
    else:
        print("\nRecord Manager is empty. Cannot delete Data")
    RECORD.close()


def do_edits(Data):
    try:
        while True:
            print("\nEnter \n1 To edit Email ID \n2 To edit Mobile number\n3 To edit the Track \n4 to exit without editing")
            ch = input()
            if ch == "1":
                new_email_id = input("\nEnter the new email address of the Candiate\n")
                Data.change_email_id(new_email_id)
                break
            elif ch == "2":
                new_phone_no = input("\nEnter the new Mobile number of the Candiate\n")
                Data.change_phone_no(new_phone_no)
                break
            elif ch == "3":
                new_address = input("\nEnter the new Track of the Candidate\n")
                Data.change_address(new_address)
                break
            else:
                print("Incorrect choice is made")
                break

    except KeyboardInterrupt:
        print("\nKeyboard Interrupt error has occurred")

    except EOFError:
        print("\nEnd of the file error has occurred")
