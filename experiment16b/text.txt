def indexed_allocation():
    f = [0] * 50  # Initialize an array of size 50 with all elements as 0

    while True:
        p = int(input("Enter index block: "))  # Input index block

        if f[p] == 0:  # If the index block is free
            f[p] = 1  # Mark the index block as allocated
            n = int(input("Enter number of files on index: "))  # Number of files to be indexed
        else:
            print("Block already allocated")
            continue  # Continue to next iteration of the loop to input new block

        inde = []  # Array to store file blocks
        for i in range(n):
            inde.append(int(input()))  # Input each file block

        # Check if any block in the index is already allocated
        allocated = False
        for i in range(n):
            if f[inde[i]] == 1:
                print("Block already allocated")
                allocated = True
                break

        if allocated:
            continue  # If any block is allocated, re-enter from the start

        # Allocate the blocks
        for j in range(n):
            f[inde[j]] = 1

        print("\nAllocated")
        print("File indexed")
        for k in range(n):
            print(f"\n{p} -> {inde[k]} : {f[inde[k]]}")

        # Ask if user wants to input more files
        c = int(input("Enter 1 to enter more files and 0 to exit: "))
        if c == 0:
            break

indexed_allocation()
