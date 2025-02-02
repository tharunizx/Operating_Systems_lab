def allocate_file():
    f = [0] * 50  # Initialize an array of size 50 with all elements as 0

    while True:
        st = int(input("\nEnter the starting block: "))  # Starting block
        length = int(input("Enter the length of the file: "))  # Length of the file

        allocated = True
        for j in range(st, st + length):
            if f[j] == 0:
                f[j] = 1
                print(f"\n{j} -> {f[j]}")
            else:
                print("Block already allocated")
                allocated = False
                break

        if allocated:
            print("\nThe file is allocated to disk")

        cont = int(input("\nDo you want to enter more files? (y-1/n-0): "))
        if cont == 0:
            break

allocate_file()
