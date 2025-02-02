MAX = 25

def main():

frag [0] MAX = *

b = [0] f = [0] * MAX * MAX

bf = [0] ff = * MAX # Block flag to mark if the block is allocated [0] * MAX # File flag to

store block number for each file print("\n\tMemory Management Scheme Worst Fit")

nbint (input("Enter the number of blocks: "))

nf int(input("Enter the number of files: "))

print("\nEnter the size of the blocks:")

for i in range (nb):

b[i] = int(input (f"Block (i+1): "))

print("Enter the size of the files:")

for i in range (nf):

f[i] = int(input(f"File (i + 1): "))

for i in range (nf):

highest-1

for j in range (nb):

if bf [j] == 0: #Check if block is not allocated

temp = b[j] if temp >= 0 and (highest == -1 of temp > b [highest] - f[i]):

- f[i]

highest = j # Store the block index of the highest fitting block

if highest != -1:

ff[i] = highest # Assign block number

frag[i] = b[highest] f[i] # Store fragmentation

bf [highest] =1# Mark block as allocated

else:

ff[i] = -1 # Not allocated

frag[i] = 1 # No fragmentation for unallocated files

for i in range(nf):

print("\nFile_no:\tFile_size:\tBlock_no:\tBlock_size:\tFragment")

if ff[i] != -1:

print (f"(i + 1}\t\t{f[i]}\t\t{ff[i] + 1}\t\t{b[ff[i]]}\t\t{frag[i]}")

else:

print(f"(i + 1}\t\t{f[i]}\t\tNot Allocated\t-\t\t-")

if name

main":

main ()