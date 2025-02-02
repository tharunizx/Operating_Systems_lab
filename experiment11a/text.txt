def one(howhung, hu, philname):
    pos = 0
    print("\nAllow one philosopher to eat at any time\n")
    for i in range(howhung):
        print(f"\nP {philname[hu[pos]]} is granted to eat")
        for x in range(pos, howhung):
            print(f"\nP {philname[hu[x]]} is waiting")
        pos += 1


def two(howhung, hu, philname):
    s = 0
    print("\nAllow two philosophers to eat at the same time\n")
    for i in range(howhung):
        for j in range(i + 1, howhung):
            if abs(hu[i] - hu[j]) >= 1 and abs(hu[i] - hu[j]) != 4:
                print(f"\n\nCombination {s + 1}\n")
                t = hu[i]
                r = hu[j]
                s += 1
                print(f"\nP {philname[hu[i]]} and P {philname[hu[j]]} are granted to eat")
                for x in range(howhung):
                    if hu[x] != t and hu[x] != r:
                        print(f"\nP {philname[hu[x]]} is waiting")


def main():
    tph = int(input("\n\nDINING PHILOSOPHER PROBLEM\nEnter the total no. of philosophers: "))
    philname = [i + 1 for i in range(tph)]  # Philosopher names are 1-indexed
    status = [1] * tph  # All philosophers are initially thinking
    hu = []  # Hungry philosophers

    howhung = int(input("How many are hungry: "))
    
    if howhung == tph:
        print("\nAll are hungry.. Deadlock stage will occur")
        print("Exiting")
        return
    else:
        for i in range(howhung):
            hu_pos = int(input(f"Enter philosopher {i + 1} position: "))
            hu.append(hu_pos)
            status[hu_pos] = 2  # Hungry philosophers are marked as status 2

        while True:
            print("1. One can eat at a time\n2. Two can eat at a time\n3. Exit")
            cho = int(input("Enter your choice: "))

            if cho == 1:
                one(howhung, hu, philname)
            elif cho == 2:
                two(howhung, hu, philname)
            elif cho == 3:
                print("Exiting...")
                break
            else:
                print("\nInvalid option..")


# Run the main function
if __name__ == "__main__":
    main()
