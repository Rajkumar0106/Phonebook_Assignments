#To Get Contact Details
def add_contact():
        name=input("Pera Sollu Da")
        phone=int(input("Enter ur phone Number"))
        email=input("Enter ur Email")
        group=input("Enter the Group like Home,Office")
    
        contact= f"{name} {phone} {email} {group}\n"

        with open("database.txt","a+") as f:
            f.write(contact)
        print("Contact Added")

def Search_Feature():
    print("Vanakkam Da, Search Engine la Irundu")
    print("1.Name")
    print("2.Group")
    Src=int(input("Choose 1 r 2"))

    y=False
    if Src==1:
        wrd=input("Enter the Name to be Searched")
        with open("database.txt") as f:
            l=f.readlines()
        for i in l:
            if wrd.lower() in i.lower():
                # print(f"Your Search {wrd} Results: ")
                print(i.strip())
    elif Src==2:
        wrd=input("Enter the Name to be Searched")
        with open("database.txt") as f:
            l=f.readlines()
        for i in l:
            if wrd.lower() in i.lower():
                # print(f"Your Search {wrd} Results: ")
                print(i.strip())
    else:
        print("Option ah olunga Sollunga Bhai")

def delete_contact():
    print("Vanthudaan da Alika")
    print("Choose the Options")
    print("1. Via Phone Number")
    print("2. Via Email")

    src = int(input("Enter your Choice: "))

    with open("database.txt", "r") as f:
        lines = f.readlines()

    new_lines = []
    found = False

    if src == 1:
        wrd = input("Enter the Phone Number: ")
        for line in lines:
            if wrd in line:
                found = True
                print(f"Contact with number {wrd} found and deleted.")
                continue  
            new_lines.append(line)

    elif src == 2:
        wrd = input("Enter the Email: ")
        for line in lines:
            if wrd in line:
                found = True
                print(f"Contact with email {wrd} found and deleted.")
                continue
            new_lines.append(line)
    else:
        print("Choice ah olunga sollu.")
        return

    if found:
        with open("database.txt", "w") as f:
            f.writelines(new_lines)
    else:
        print("Contact not found. Nothing deleted.")


#Starts the Program
def main():
    while True:
        print("Vannakam Da Mappula")
        print("Choice ah sollu da venna")
        print("1.Contanct Solren")
        print("2.Data Venum Da Venna")
        print("3.Delete Panithu Po Da")
        print("4.Kelmburen")
        c=int(input("Choose the Option 1 r 2 r 3 r 4 "))
        
        if c==1:
             add_contact()
        elif c==2:
             Search_Feature()
             break
        elif c==3:
             delete_contact()
             break
        elif c==4:
             print("Apudi orama poda venna") 
             break
        else:
             print("Choise ah olunga solra venna")

main()