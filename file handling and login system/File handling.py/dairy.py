import os
print("\nEnter 1 to write in dairy ")
print("\nEnter 2 to read the dairy ")
print("\nEnter 3 to delete the dairy ")

choice =int(input("Enter the choice :"))

if choice == 1:
    writes = input("Now you can write any thing you want :")
    f=open("My Dairy.txt","a")
    f.write(writes)
    f.write("\n____________________________________________________\n")
    f.close

elif choice == 2:
    f=open("My Dairy.txt","r")
    print(f.read())   

elif choice == 3:
   a = input("Are you sure you want to delete the dairy :")
   if a == "yes" or a == "Yes":
    os.remove("My Dairy.txt")
    print("Dairy removed")
   else:
      print("not removed") 