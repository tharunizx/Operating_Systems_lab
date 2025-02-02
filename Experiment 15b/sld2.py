class Directory:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.subdirectories = {}

def main():
    root_directory_name = input("Enter name of root directory -- ")
    root_directory = Directory(root_directory_name)

    current_directory = root_directory

    while True:
        print("1. Create File 2. Delete File 3. Search File 4. Display Files 5. Create Subdirectory 6. Enter Subdirectory 7. Exit")
        choice = input("Enter your choice – ")

        if choice == '1':
            file_name = input("Enter the name of the file -- ")
            if file_name not in current_directory.files:
                current_directory.files.append(file_name)
                print(f"File {file_name} created.")
            else:
                print(f"File {file_name} already exists.")

        elif choice == '2':
            file_name = input("Enter the name of the file -- ")
            if file_name in current_directory.files:
                current_directory.files.remove(file_name)
                print(f"File {file_name} is deleted.")
            else:
                print(f"File {file_name} not found.")

        elif choice == '3':
            file_name = input("Enter the name of the file -- ")
            if file_name in current_directory.files:
                print(f"{file_name} found.")
            else:
                print(f"{file_name} not found.")

        elif choice == '4':
            if current_directory.files:
                print("The Files are --", " ".join(current_directory.files))
            else:
                print("No files found.")

        elif choice == '5':
            subdirectory_name = input("Enter the name of the subdirectory -- ")
            if subdirectory_name not in current_directory.subdirectories:
                current_directory.subdirectories[subdirectory_name] = Directory(subdirectory_name)
                print(f"Subdirectory {subdirectory_name} created.")
            else:
                print(f"Subdirectory {subdirectory_name} already exists.")

        elif choice == '6':
            subdirectory_name = input("Enter the name of the subdirectory to enter -- ")
            if subdirectory_name in current_directory.subdirectories:
                current_directory = current_directory.subdirectories[subdirectory_name]
                print(f"Entered subdirectory {subdirectory_name}.")
            else:
                print(f"Subdirectory {subdirectory_name} not found.")

        elif choice == '7':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
