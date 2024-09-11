#Leonardo Nava 
# 9/11/24
#hold the options that user can do to thier contacts

def print_list(contacts_list):
    #print("CONTACTS LIST  ")
    print(f"{'Index':<8}{'First Name':<22}{'Last Name':<22}")
    for i in range(len(contacts_list)):
        print(f'{str(i):8}{contacts_list[i][0]:22}{contacts_list[i][1]:22}')
    
def add_contact(contacts_list):
   # print("ADD CONTACT")
    first_name = input("what is your first name? ")
    last_name = input("what is your last name? ")
    contacts_list.append([first_name, last_name])
    return contacts_list    

def modify_contact(contacts_list):
   # print("MODIFY CONTACT")
    try:
        index = int(input("enter the index number of who you change? "))
        first_name = input("what is your first name? ")
        last_name = input("what is your last name? ")
        
        if 0 <= index <len(contacts_list):

            contacts_list[index] = [first_name,last_name]
        else: 
            print("Invalid index number.")
    except ValueError:
        print("Invalid input. Put a number ")
    return contacts_list
            
      

def delete_contact(contacts_list):
    #print("DELETE CONTACT")
    try:
        index = int(input("What contact are you deleting? "))
        if 0<= index < len(contacts_list):
            del contacts_list[index]
        else:
            print("Invalid index number.")
    except ValueError:
        print("invalid input, put  a number ")
    return contacts_list


def sort_contacts(contacts_list, column=0):
    if(column == 0 ):
        return sorted(contacts_list, key=lambda contact: contact[0])
    elif column == 1:
        # Sort by last name (index 1)
        return sorted(contacts_list, key=lambda contact: contact[1])
    else:
        print("Invalid column. Use 0 for first name or 1 for last name.")
        return contacts_list
        
    
    

#def sort_first(contacts_list ):
    # by defualt it just sorts the names in alpha via first name
  #  sort_first = sorted(contacts_list)
 #   contacts_list = sort_first
   # return contacts_list

###
#def sort_last(contacts_list):
    #need this line so it can see that we talking about last names 
  #  sort_last = sorted(contacts_list, key=lambda contact: contact[1])
 #   contacts_list = sort_last
   # return contacts_list
 ### 