def main():
    t = [0] * 20  # Initialize a list to store the track numbers
    tohm = [0] * 20  # Initialize a list to store the difference between track movements
    tot = 0  # Total header movement
    n = int(input("Enter the number of tracks: "))  # Number of tracks to be traversed

    print("Enter the tracks to be traversed:")
    for i in range(2, n + 2):
        t[i] = int(input())  # Input the tracks

    # Calculate the difference between consecutive tracks (header movements)
    for i in range(1, n + 1):
        tohm[i] = t[i + 1] - t[i]
        if tohm[i] < 0:
            tohm[i] = -tohm[i]  # Take absolute value of the difference

    # Calculate the total and average header movements
    for i in range(1, n + 1):
        tot += tohm[i]
    avhm = float(tot) / n

    # Display the tracks traversed and the difference between tracks
    print("Tracks traversed\tDifference between tracks")
    for i in range(1, n + 1):
        print(f"{t[i]}\t\t\t{tohm[i]}")

    # Display the average header movements
    print(f"\nAverage header movements: {avhm}")

# Run the main function
if __name__ == "__main__":
    main()
