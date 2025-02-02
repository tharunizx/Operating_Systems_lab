def main():
    ms = int(input("Enter the total memory available (in Bytes)-- "))
    temp = ms
    mp = []
    n = 0
    ch = 'y'
    while ch == 'y':
        mem_req = int(input(f"Enter memory required for process {n+1} (in Bytes) -- "))
        mp.append(mem_req)
        if mem_req <= temp:
            print(f"Memory is allocated for Process {n+1}")
            temp -= mem_req
            n += 1
        else:
            print("Memory is Full")
            break
        ch = input("Do you want to continue(y/n) -- ").strip()
    print(f"Total Memory Available -- {ms}")
    print("\tPROCESS\t\t MEMORY ALLOCATED ")
    for i in range(n):
        print(f"\t{i+1}\t\t{mp[i]}")
    print(f"Total Memory Allocated is {ms-temp}")
    print(f"Total External Fragmentation is {temp}")
if __name__ == "__main__":
    main()
