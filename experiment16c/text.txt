def contiguous_allocation():
    f = [0] * 50  # Initialize an array of size 50 with all elements as 0

    # Input how many blocks are already allocated
    p = int(input("Enter how many blocks that are already allocated: "))
    print("\nEnter the block numbers that are already allocated:")
    
    for i in range(p):
        a = int(input())  # Input each allocated block
        f[a] = 1  # Mark them as allocated

    while True:
        # Input starting index block and length of file
        st = int(input("Enter the starting index block: "))
        length = int(input("Enter the length of the file: "))

        k = length
        for j in range(st, st + k):
            if f[j] == 0:
                f[j] = 1  # Mark the block as allocated
                print(f"\n{j} -> {f[j]}")
            else:
                print(f"\n{j} -> File is already allocated")
                k += 1  # Increase the range to allocate the file in next available block

        # Ask if the user wants to enter more files
        c = int(input("\nDo you want to enter one more file? (yes-1/no-0): "))
        if c == 0:
            break

contiguous_allocation()
