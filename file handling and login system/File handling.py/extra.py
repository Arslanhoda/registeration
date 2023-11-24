#  import os

# while True:
#     print("\n1. Add record")
#     print("2. Display ALL Record")
#     print("3. Search student record by name")
#     print("4. Search student record by rollno")
#     print("5. Exit")
    
#     choice = int(input("Enter choice: "))

#     if choice == 5:
#         break
#     elif choice == 1:
#         name = input("\nEnter Student Name: ")
#         rollno = input("Enter Student Rollno: ")
#         student_class = input("Enter Student class: ")
#         fees = input("Enter Student fees: ")
#         percentage = input("Enter Student percentage: ")
#         f=open("developer.txt", "a")
#         f.write(+name+"-"+rollno+"-"+student_class+"-"+fees+"-"+percentage+"\n")
#         f.close
#     elif choice == 2:
#         print("\n\nList of present records\n")
#         print("NAME-ROLLNO-CLASS-FEES-PER")
#         f=open("developer.txt", "r")
#         while(True):
#             d=f.readline()
#             l=len(d)
#             if l==0:
#                 break
#             print(d.strip())
#         f.close        
#     elif choice == 3:
#         search_name = input("Enter student name: ")
#         f=open("developer.txt", "r")
#         flag = 0
#         while True:
#          t=f.readline()
#          l=len(t)
#          if t==0:
#             break
#          g=t.split("-")
#          if g[0] == search_name:
#           print("\nRecord found")
#           print("Name:", g[0])
#           print("Rollno:", g[1])
#           print("Class:", g[2])
#           print("Fees:", g[3])
#           print("Percentage:", g[4])
#           flag = 1
#           break
#         if flag == 0:
#          print("Record not found")
#     elif choice == 3:
#         search_name = input("Enter student name: ")
#         f=open("developer.txt", "r")
#         flag = 0
#         while True:
#          t=f.readline()
#          l=len(t)
#          if t==0:
#             break
#          g=t.split("-")
#          if g[0] == search_name:
#           print("\nRecord found")
#           print("Name:", g[0])
#           print("Rollno:", g[1])
#           print("Class:", g[2])
#           print("Fees:", g[3])
#           print("Percentage:", g[4])
#           flag = 1
#           break
#         if flag == 0:
#          print("Record not found")
# import os

# def update_record():
#     search = input("Enter student rollno to update data: ")
#     file_path = "developer.txt"

#     with open(file_path, "r") as file:
#         lines = file.readlines()

#     found = False
#     updated_data = []

#     for line in lines:
#         data = line.strip().split('-')
#         if data[3] == search:
#             found = True
#             print("\nRecord found. Enter updated information:")
#             n = input("Enter Student Name: ")
#             fn = input("Enter Student Father Name: ")
#             phone = input("Enter Student Phone no: ")
#             cl = input("Enter Student Class: ")
#             sec = input("Enter Student Section: ")
#             fees = input("Enter Student Fees: ")
#             per = input("Enter Student Percentage: ")
#             ads = input("Enter Student Address: ")
#             updated_data.append(f"{n}-{fn}-{phone}-{cl}-{sec}-{fees}-{per}-{ads}\n")
#         else:
#             updated_data.append(line)

#     if not found:
#         print("Record not found.")
#     else:
#         with open(file_path, "w") as file:
#             file.writelines(updated_data)
#         print("Record updated successfully.")

# z = 1
# while True:
#     print("\n1. Add record")
#     print("2. Display ALL Record")
#     print("3. Search student record by name")
#     print("4. Search student record by rollno")
#     print("5. Search student record by father name")
#     print("6. Update student record")
#     print("7. Exit")

#     choice = int(input("Enter choice: "))

#     if choice == 7:
#         print("Bye")
#         break
#     elif choice == 1:
#         # Code for adding a record
#         # ...
#     elif choice == 2:
#         # Code for displaying all records
#         # ...
#     elif choice == 3:
#         # Code for searching by name
#         # ...
#     elif choice == 4:
#         # Code for searching by rollno
#         # ...
#     elif choice == 5:
#         # Code for searching by father name
#         # ...
#     elif choice == 6:
#         # Code for updating record
#         update_record()
#     else:
#         print("Invalid choice. Please enter a valid option.")
# c=input("Enter:")
# if c==6:
#     search =input("Enter student name :")
#     f=open("developer.txt","r") 
#     flag=0
#     while(True):
#         t=f.readline()
#         l=len(t)
#         if l == 0:
#             break
#         g=t.split('-')
#         if(g[0]==search):
#             n=input("\n Enter Student Name :")
#             fn=input("\n Enter Student father Name :")
#             phone=input("\n Enter Student phone no :")
#             r=input("\n Enter Student Rollno :")
#             cl=input("\n Enter Student class :")
#             sec=input("\n Enter Student section :")
#             fees=input("\n Enter Student fees :")
#             per=input("\n Enter Student percentage :")
#             ads=input("\n Enter Student adress :")
#             f=open("developer.txt","a")
#             f.write()
#             f==1
#             break
#         f.close
#         if flag == 0:
#             print("Record not found"

#     elif choice == 7:
#         delete_name = input("Enter student name to delete: ")
#         with open("developer.txt", "r") as file:
#             lines = file.readlines()
#         with open("developer.txt", "w") as file:
#             flag = False
#             for line in lines:
#                 data = line.split('-')
#                 if data[0] != delete_name:
#                     file.write(line)
#                 else:
#                     flag = True
#             if flag:
#                 print("Record deleted")
#             else:
#                 print("Record not found")

#     else:
#         print("Invalid choice. Please enter a valid option.")





                                        # file handling