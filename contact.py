import csv
path="contact.csv"
def add():
    print("\n----Add Contact----")
    name=input("\nEnter Name: ")
    number=input("\nEnter Phone Number:")

    with open(path,mode="r") as file:
        if file.read()=="":
            with open(path,mode="a") as file_app:
                file_app.write("Name,Phone\n")

    with open(path, mode="a") as file:
        file.write(f"{name},{number}\n")
    print(f"\n contact for {name} saved succesfully! \n")

def view():
    print("\n----View Contacts----")
    with open(path, mode="r")as file:
        print(file.read())
    while(1):
        print("\n1.Update\n2.Delete\n3.Back")
        opt=int(input("\nSelect Option between 1 to 3: "))
        if opt==1:
            name=input("Enter Name:")
            update(name)
            break
        elif opt==2:
            name=input("Enter Name: ")
            delete(name)
            break
        else:
            break

def search():
    print("\n----Search Contact----")
    name=input("Enter Name:")
    with open(path,"r") as file:
        li=file.readlines()
    for i in li:
        c_name,c_num=i.split(",")
        if c_name==name:
            print("\nContact Found!")
            print(f"{name}:{c_num}")
            while(1):
                print("\n1.Update\n2.Delete\n3.Back")
                opt=int(input("\nSelect appropriate option: "))
                if opt==1:
                    update(name)
                    break
                elif opt==2:
                    delete(name)
                    break
                else:
                    break

def update(name):
    
    with open(path,"r")as file:
        con=file.readlines()
    
    with open(path,"w")as file:
        for c in con:
            c_name,c_num=c.split(",")
            if name==c_name:
                print(f"your previous data- \nname:{c_name}\nnumber:{c_num}")
                number=input("enter new number: ")
                file.write(f"{c_name},{number}")
                print("contact updated!")
            else:
                file.write(f"{c_name},{c_num}")
    with open(path,"r")as file:
        print("\n",file.read())

def delete(name):
    with open(path,"r") as file:
        li=file.readlines()
    with open(path,"w") as file:
        for i in li:
            c_name,c_num=i.split(",")
            if c_name!=name:
                file.write(f"{c_name},{c_num}")
            else:
                print(f"\ncontact for {c_name} deleted successfully! ")

while(1):
    print("\n1.Add\n2.View All\n3.Search\n4.exit")
    opt=int(input("\nselect option between 1 to 4: "))
    if opt==1:
        add()
    elif opt==2:
        view()
    elif opt==3:
        search()
    elif opt==4:
        print("Thanks For Using Bye!")
        break
    else:
        print("! enter valid input between 1 to 4!")
