class StudentRecordSystem:
    def __init__(self):
        self.file_path = "developer.txt"

    def add_record(self):
        n = input("\nEnter Student Name: ")
        fn = input("\nEnter Student Father Name: ")
        phone = input("\nEnter Student Phone no: ")
        r = input("\nEnter Student Rollno: ")
        cl = input("\nEnter Student Class: ")
        sec = input("\nEnter Student Section: ")
        fees = input("\nEnter Student Fee: ")
        per = input("\nEnter Student Percentage: ")
        ads = input("\nEnter Student Address: ")

        f=open(self.file_path, "a")
        f.write(f"{n}-{fn}-{phone}-{r}-{cl}-{sec}-{fees}-{per}-{ads}\n")

    def display_all_records(self):
        print("\n\nList of present records\n\n")
        print("Name-Father Name-Roll No-Class-Fee-Percentage-Address")

        f=open(self.file_path, "r")
        for line in f:
          print(line.strip())

    def search_by_name(self):
        search = input("Enter student name: ")
        f=open(self.file_path, "r") 
        for line in f:
            data = line.split('-')
            if data[0] == search:
                self.display_student_info(data)
                return
        print("Record not found")

    def search_by_roll_no(self):
        search = input("Enter student Roll NO: ")
        with open(self.file_path, "r") as f:
            for line in f:
                data = line.split('-')
                if len(data) >= 4 and data[3] == search:
                    self.display_student_info(data)
                    return
        print("Record not found")

    def search_by_father_name(self):
        search = input("Enter student Father Name: ")
        with open(self.file_path, "r") as f:
            for line in f:
                data = line.split('-')
                if len(data) >= 2 and data[1] == search:
                    self.display_student_info(data)
                    return
        print("Record not found")

    def update_record(self):
        search = input("Enter student name: ")
        with open(self.file_path, "r") as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            data = line.strip().split('-')
            if data[0] == search:
                lines.pop(i)
                self.add_record_to_lines(lines)
                return
        print("Record not found")

    def delete_record(self):
        delete_name = input("Enter student name to delete: ")
        with open(self.file_path, "r") as f:
            lines = f.readlines()

        with open(self.file_path, "w") as f:
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

    def add_record_to_lines(self, lines):
        n = input("\nEnter Student Name: ")
        fn = input("Enter Student Father Name: ")
        phone = input("Enter Student Phone no: ")
        r = input("Enter Student Rollno: ")
        cl = input("Enter Student Class: ")
        sec = input("Enter Student Section: ")
        fees = input("Enter Student Fee: ")
        per = input("Enter Student Percentage: ")
        ads = input("Enter Student Address: ")

        new_record = f"{n}-{fn}-{phone}-{r}-{cl}-{sec}-{fees}-{per}-{ads}\n"
        lines.append(new_record)

        with open(self.file_path, "w") as f:
            f.writelines(lines)

    def display_student_info(self, data):
        print("\nRecord found")
        print("Student name is", data[0])
        print("Father name is", data[1])
        print("Phone no", data[2])
        print("Roll No is", data[3])
        print("Class is", data[4])
        print("Section is", data[5])
        print("Fee is", data[6])
        print("Percentage is", data[7])


if __name__ == "__main__":
    record_system = StudentRecordSystem()

    while True:
        print("\n1. Add record")
        print("2. Display all records")
        print("3. Search student record by name")
        print("4. Search student record by rollno")
        print("5. Search student record by father name")
        print("6. Update record")
        print("7. Delete student record")
        print("8. Exit")

        choice = int(input("Enter choice: "))

        if choice == 8:
            print("Bye")
            break
        elif choice == 1:
            record_system.add_record()
        elif choice == 2:
            record_system.display_all_records()
        elif choice == 3:
            record_system.search_by_name()
        elif choice == 4:
            record_system.search_by_roll_no()
        elif choice == 5:
            record_system.search_by_father_name()
        elif choice == 6:
            record_system.update_record()
        elif choice == 7:
            record_system.delete_record()
