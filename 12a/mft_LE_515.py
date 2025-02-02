def main():
    ms = int(input("Enter the total memory available (in Bytes) -- "))
    bs = int(input("Enter the block size (in Bytes) -- "))
    nob = ms // bs
    ef = ms - nob * bs
    n = int(input("Enter the number of processes -- "))
    mp = []
    for i in range(n):
        mem_req = int(input(f"Enter memory required for process {i+1} (in Bytes)-- "))
        mp.append(mem_req)
    print(f"No. of Blocks available in memory--{nob}")
    print("PROCESS\tMEMORY REQUIRED\tALLOCATED\tINTERNAL FRAGMENTATION")
    tif = 0  # Total internal fragmentation
    p = 0    # Number of allocated processes
    for i in range(n):
        print(f"{i+1}\t\t{mp[i]}", end="")
        if mp[i] > bs:
            print("\t\tNO\t\t---")
        else:
            print(f"\t\tYES\t{bs - mp[i]}")
            tif += bs - mp[i]
            p += 1
        if p >= nob:
            break
    if p < n:
        print("Memory is Full, Remaining Processes cannot be accommodated")
    print(f"Total Internal Fragmentation is {tif}")
    print(f"Total External Fragmentation is {ef}")
if __name__ == "__main__":
    main()
