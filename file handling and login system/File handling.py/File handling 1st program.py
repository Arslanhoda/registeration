import os
z=1
while(True):
    print("\n1.Add record")
    print("\n2.Display ALL Record")
    print("\n3.search student record by name")
    print("\n4.search student record by rollno")
    print("\n5.search student record by father name")
    print("\n6.update record")
    print("\n7.Delete student record")
    print("\n8.Exit")
    c=int(input("Enter choice :"))
    if c == 8:
        print("Bye")
        break
    elif c == 1:
        n=input("\n Enter Student Name :")
        fn=input("\n Enter Student Father Name :")
        phone=input("\n Enter Student Phone no :")
        r=input("\n Enter Student Rollno :")
        cl=input("\n Enter Student Class :")
        sec=input("\n Enter Student Section :")
        fees=input("\n Enter Student Fee :")
        per=input("\n Enter Student Percentage :")
        ads=input("\n Enter Student Address :")
        f=open("developer.txt","a")
        f.write(n+"-"+fn+"-"+phone+"-"+cl+"-"+sec+"-"+fees+"-"+per+"-"+ads+"\n")
        f.close()
    elif c == 2:
        print("\n\n list of present record\n\n")
        print("Name-Father Name-Roll No-Class-Fee-Percentage-Address")
        f=open("developer.txt","r")
        while(True):
            d=f.readline()
            l=len(d)
            if l==0:
                break
            print(d.strip())
        f.close()    
    elif c == 3:
        search =input("Enter student name :")
        f=open("developer.txt","r") 
        flag=0
        while(True):
            t=f.readline()
            l=len(t)
            if l == 0:
                break
            g=t.split('-')
            if(g[0]==search):
                print("\n Record found")
                print("Student name is",g[0])
                print("Father name is",g[1])
                print("Phone no",g[2])
                print("Roll No is",g[3])
                print("Class is",g[4])
                print("Section is",g[5])
                print("Fee is",g[6])
                print("Percentage is",g[7])
                flag=1
                break
            f.close
        if flag == 0:
            print("Record not found")
    elif c == 4:
     search = input("Enter student Roll NO: ")
     f = open("developer.txt", "r") 
     flag = 0
     while True:
         t = f.readline()
         if not t:  # Check if t is an empty string
            break
         g = t.split('-')
         if len(g) >= 4 and g[3] == search:
             print("\nRecord found")
             print("Student Name is", g[0])
             print("Father name is", g[1])
             print("Phone No", g[2])
             print("Roll No is", g[3])
             print("Class is", g[4])
             print("Section is", g[5])
             print("Fee is", g[6])
             print("Percentage is", g[7])
             flag = 1
             break
         
     f.close()
     if flag == 0:
        print("Record not found")

    elif c == 5:
     search = input("Enter student Father Name: ")
     f = open("developer.txt", "r") 
     flag = 0
     while True:
         t = f.readline()
         if not t:
            break
         g = t.split('-')
         if len(g) >= 2 and g[1] == search:
             print("\nRecord found")
             print("Student Name is", g[0])
             print("Father name is", g[1])
             print("Phone No", g[2])
             print("Roll No is", g[3])
             print("Class is", g[4])
             print("Section is", g[5])
             print("Fee is", g[6])
             print("Percentage is", g[7])
             flag = 1
             break
         
     f.close()
     if flag == 0:
        print("Record not found")
   
    elif c == 6:
        search = input("Enter student name: ")
        f = open("developer.txt", "r")
        lines = f.readlines()
        f.close()

        flag = False
        for i, line in enumerate(lines):
            data = line.strip().split('-')
            if data[0] == search:
                flag = True
                lines.pop(i)
                break

        if flag:
            n = input("\nEnter Student Name: ")
            fn = input("Enter Student father Name: ")
            phone = input("Enter Student phone no: ")
            r = input("Enter Student Rollno: ")
            cl = input("Enter Student class: ")
            sec = input("Enter Student section: ")
            fees = input("Enter Student fees: ")
            per = input("Enter Student percentage: ")
            ads = input("Enter Student address: ")

            new_record = f"{n}-{fn}-{phone}-{r}-{cl}-{sec}-{fees}-{per}-{ads}\n"
            lines.append(new_record)

            f = open("developer.txt", "w")
            f.writelines(lines)
            f.close()
        else:
            print("Record not found")
    elif c == 7:
     delete_name = input("Enter student name to delete: ")
     with open("developer.txt", "r") as f:
        lines = f.readlines()

     with open("developer.txt", "w") as f:
        flag = False
        for line in lines:
            data = line.split('-')
            if data[0] != delete_name:
                f.write(line)
            else:
                flag = True

        if flag:
            print("Record deleted")
        else:
            print("Record not found")
