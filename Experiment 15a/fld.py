class Directory:
    def __init__(self, name):
        self.name = name
        self.files = []
def main():
    directory_name = input("Enter name of directory -- ")
    directory = Directory(directory_name)
    while True:
        print("\n1. Create File 2. Delete File 3. Search File 4. Display Files 5. Exit")
        choice = input("Enter your choice – ")
        if choice == '1':
            file_name = input("Enter the name of the file -- ")
            if file_name not in directory.files:
                directory.files.append(file_name)
                print(f"File {file_name} created.")
            else:
                print(f"File {file_name} already exists.")

        elif choice == '2':
            file_name = input("Enter the name of the file -- ")
            if file_name in directory.files:
                directory.files.remove(file_name)
                print(f"File {file_name} is deleted.")
            else:
                print(f"File {file_name} not found.")

        elif choice == '3':
            file_name = input("Enter the name of the file -- ")
            if file_name in directory.files:
                print(f"{file_name} found.")
            else:
                print(f"{file_name} not found.")

        elif choice == '4':
            if directory.files:
                print("The Files are --", " ".join(directory.files))
            else:
                print("No files found.")

        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
