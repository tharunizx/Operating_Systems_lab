MAX = 25


def main():

frag [0] MAX =

*

b = [0] * MAX

f = [0] bf = [0] * MAX

* MAX # Block flag to mark if the block is allocated

ff = [0] * MAX # File flag to store block number for each file

print("\n\tMemory Management Scheme First Fit")

nbint (input("Enter the number of blocks: "))

nf int(input("Enter the number of files: "))

print("\nEnter the size of the blocks:")

for i in range (nb):

b[i] = int(input(f"Block (i + 1}: "))

print("Enter the size of the files:")

for i in range (nf):

f[i] = int(input(f"File (i + 1): "))

for i in range (nf):

for j in range (nb): if bf [j] == 0: #Check if block is not allocated

temp = b[j]

if temp >= 0:

ff[i]

=

f[i]

j# Assign block number

frag [i] bf[ff[i]] = 1 # Mark block as allocated

=

temp # Store fragmentation

break # Move to the next file after allocation print("\nFile_no:\tFile_size:\tBlock_no:\tBlock_size:\tFragment")

for i in range (nf):

if ff[i] != 0 or frag[i] != 0:

print (f"(i + 1}\t\t{f[i]}\t\t{ff[i] + 1}\t\t{b[ff[i]]}\t\t{frag[i])")

else:

print (f" (i + 1}\t\t{f[i]}\t\tNot Allocated\t-\t\t-")

if name == main":

main()