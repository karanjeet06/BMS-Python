import csv,os
#admin login
def page():
    while True:
        print("********************************")
        print("1-admin login ")
        print("2-customer login")
        print("3-exit ")
        n=int(input("enter your choice : "))
        if (n==1):
            admin_login()
        elif(n==2):
            customer_login()
        else:   
            print("exit")
        return 0
def admin_login():
    username=input("enter username : ")
    password=input("enter password : ")
    file=open("adminfile.csv","r")
    file_reader=csv.reader(file)
    for i in file_reader:
        if (i[0]==username):
            if(i[1]==password):
                print("login success")
                admin_menu()
    file.close()
def admin_menu():
    print("*****************************")
    print("1-add items")
    print("2-remove items")
    print("3- update")
    print("4- view items")
    n=int(input("enter the choice : "))
    if (n==1):
        add_items()
    elif (n==2):
        remove()
    elif(n==3):
        update()
    elif(n==4):
        view_items()
    else:
        return 0
def add_items():
    n=int(input("enter the number of items : "))
    file=open("menu_file.csv","a",newline='')
    write=csv.writer(file)
    for i in range(0,n):
        item_name=input("enter item : ")
        item_price=input("enter price : ")
        item_quantity=input("enter the quantity : ")
        data=[item_name,item_price,item_quantity] 
        write.writerow(data)
    file.close()
def remove():
    itemName=input("enter the item : ")
    file=open("menu_file.csv","r")
    file1=open("tempfile.csv","w",newline='')
    read=csv.reader(file)
    found=0
    for i in read:
        if (i[0]==itemName):
           found=1
           continue;
        write=csv.writer(file1)
        write.writerow(i);
    file.close()
    file1.close()
    if (found==1):
        os.remove("menu_file.csv")
        os.rename("tempfile.csv","menu_file.csv")
    return 0
def update():
    itemName=input("enter item : ")
    file=open("menu_file.csv","r")
    file1=open("temp_file.csv","w",newline='')
    read=csv.reader(file)
    found=0
    for i in read:
        if (i[0]==itemName):
            found=1
            itemPrice=int(input("enter the price : "))
            itemQuantity=int(input("enter the quantity : "))
            write=csv.writer(file1)
            write.writerow([i[0],itemPrice,itemQuantity])
            continue
        write=csv.writer(file1)
        write.writerow(i)
    file.close()
    file1.close()
    if (found==1):
        os.remove("menu_file.csv")
        os.rename("temp_file.csv","menu_file.csv")
    return 0
def view_items():
    file=open("menu_file.csv","r")
    read=csv.reader(file)
    for i in read:
        print(i)
 #view menu buy view order update order -remove,add
def customer_login():
    print("****************************")
    print("1-view menu")
    print("2-buy items")
    print("3-view ordeers")
    print("4-update order")
    n= int(input("enter the choice : "))
    if (n==1):
        viewMenu()
    elif (n==2):
        buyItems()
    elif (n==3):
        viewOrder()
    elif(n==4):
        updateOrder()
    else:
        print("wrong choice") 
def viewMenu():
    file=open("menu_file.csv","r")
    read=csv.reader(file)
    for i in read:
        print(i)
def buyItems():
    itemName=input("enter the item : ")
    file=open("Menu_file.csv","r")
    file2=open("customerFile.csv","a",newline='')
    read=csv.reader(file)
    for i in read:
        if (i[0]==itemName):
            q=input("enter quantity  :")
            write=csv.writer(file2)
            write.writerow([itemName,i[1],q])
            continue
    file.close()
    file2.close()
def viewOrder():
    file2=open("customerFile.csv","r")
    read=csv.reader(file2)
    for i in read:
        print(i)
def updateOrder():
    print("**********")
    print("1-add items")
    print("2-remove items")
    n=int(input("enter choice : "))
    if (n==1):
        addItems()
    elif(n==2):
        removeitems()
    else:
        return 0
def addItems():
    itemname=input("enter the item : ")
    itemQuant=int(input("enter the quantity : "))
    file=open("customerFile.csv","r")
    file0=open("menu_file.csv","r")
    file1=open("tempFile.csv","a",newline='')
    read=csv.reader(file0)
    read1=csv.reader(file)
    write=csv.writer(file1)
    found=0
    for i in read:
        if (i[0]==itemname):
            found=1
            write.writerow([i[0],i[1],itemQuant])
        for j in read1:
            write.writerow(j)
    file.close()
    file1.close()
    if (found==1):
        os.remove("customerFile.csv")
        os.rename("tempFile.csv","customerFile.csv")
def removeitems():
    itemname=input("enter item : ")
    file=open("customerFile.csv","r")
    file1=open("tempfile.csv","w")
    read=csv.reader(file)
    found=0
    for i in read:
        if (i[0]==itemname):
            found=1
            continue
        write=csv.writer(file1)
        write.writerow(i);
    file.close();
    file1.close();
    if (found==1):
        os.remove("customerFile.csv")
        os.rename("tempfile.csv","customerFile.csv")
page()