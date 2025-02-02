def main():
    t = [0] * 20  # List to store track positions
    d = [0] * 20  # List to store differences between adjacent tracks
    atr = [0] * 20  # List to store the arranged track traversal
    sum_movements = 0  # To store the sum of header movements

    n = int(input("Enter the number of tracks to be traversed: "))
    h = int(input("Enter the position of the head: "))
    
    t[0] = 0  # First element is 0 (as in the C code)
    t[1] = h  # Second element is the head position
    
    print("Enter the tracks:")
    for i in range(2, n + 2):
        t[i] = int(input())

    # Sorting the tracks using Bubble Sort (similar to the original C code)
    for i in range(n + 2):
        for j in range((n + 2) - i - 1):
            if t[j] > t[j + 1]:
                temp = t[j]
                t[j] = t[j + 1]
                t[j + 1] = temp

    # Finding the head position in the sorted list
    for i in range(n + 2):
        if t[i] == h:
            j = i
            k = i

    p = 0
    # Arrange the traversal for the tracks before the head
    while t[j] != 0:
        atr[p] = t[j]
        j -= 1
        p += 1

    atr[p] = t[j]  # Add track 0 (since we hit the start of the list)
    
    # Arrange the traversal for the tracks after the head
    for p in range(k + 1, n + 2):
        atr[p] = t[k + 1]
        k += 1

    # Calculate header movements
    for j in range(n + 1):
        if atr[j] > atr[j + 1]:
            d[j] = atr[j] - atr[j + 1]
        else:
            d[j] = atr[j + 1] - atr[j]
        sum_movements += d[j]

    # Calculate and print the average header movements
    print(f"\nAverage header movements: {float(sum_movements) / n}")

# Run the main function
if __name__ == "__main__":
    main()
