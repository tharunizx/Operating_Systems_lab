def main():
    t = [0] * 20  # Array to store track positions
    d = [0] * 20  # Array to store differences between adjacent tracks
    atr = [0] * 20  # Array to store the arranged track traversal
    sum_movements = 0  # To store the sum of header movements

    n = int(input("Enter the number of tracks to be traversed: "))
    h = int(input("Enter the position of head: "))
    
    # Initialize the array with the first two known positions
    t[0] = 0  # First position is 0 (beginning)
    t[1] = h  # Second position is the head
    
    tot = int(input("Enter total number of tracks: "))
    t[2] = tot - 1  # The last track (tot - 1)
    
    print("Enter the tracks:")
    for i in range(3, n + 3):
        t[i] = int(input())  # Read the tracks
    
    # Sort the tracks using bubble sort
    for i in range(n + 3):
        for j in range(n + 3 - i - 1):
            if t[j] > t[j + 1]:
                temp = t[j]
                t[j] = t[j + 1]
                t[j + 1] = temp
    
    # Find the index of the head position in the sorted list
    for i in range(n + 3):
        if t[i] == h:
            j = i
            break

    p = 0
    # Traverse from the head to the end (tot - 1)
    while t[j] != tot - 1:
        atr[p] = t[j]
        j += 1
        p += 1
    
    atr[p] = t[j]  # Add the last track (tot - 1)
    p += 1

    # Traverse from the beginning to the head
    i = 0
    while p != (n + 3) and t[i] != h:
        atr[p] = t[i]
        i += 1
        p += 1

    # Calculate the total header movements
    for j in range(n + 2):
        if atr[j] > atr[j + 1]:
            d[j] = atr[j] - atr[j + 1]
        else:
            d[j] = atr[j + 1] - atr[j]
        sum_movements += d[j]

    # Print the total header movements and the average
    print(f"Total header movements: {sum_movements}")
    print(f"Average header movements: {float(sum_movements) / n}")

# Run the main function
if __name__ == "__main__":
    main()
