def cnt_take():
    with open("contact_book.txt","a")as f:
        n1 = input("Enter contact in contact book: ")
        l1 = [n1]
        
        f.write(str(l1))
        print("Record added")

def cnt_read():
    print("**************record**************")
    with open("contact_book.txt","r")as f:
        read = f.read()
        print(read)

def cnt_remove():
    with open("contact_book.txt","w")as f:
        print("record deleted")

def menu():
    while True:
        
        print("""1. ADD 
2. READ 
3. REMOVE""")
        n2 = int(input("Choose from above: "))

        if n2 == 1:
            cnt_take()

        elif n2 == 2:
            cnt_read()
        elif n2 == 3:
            cnt_remove()

        choose = input("Do you wanna continue(y/n): ")
        if choose == 'y':
            menu()
        else:
            break
        

menu()
    




